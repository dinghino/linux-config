# -*- coding: utf-8 -*-
import copy
import json

import arrow
import click
import six


class StateManager(object):
    """
    An StateManager object handles and keep track of both the persistent
    app state and the runtime options and state, such as options structure,
    installation status etc and takes care of handling reading and saving on
    the persistent app state.

    Arguments:
        ctx (:any:`AppManager`): Application manager context.
        state_path (int): Absolute path to the persistent state file to handle.

    """

    def __init__(self, ctx, state_path):
        self.ctx = ctx
        self.state = None
        self.state_path = state_path

        self.load()

    # ##############################
    # Persistent state file handlers

    def load(self, path=None):
        """
        Load a persistent application state from the given path.

        Args:
            path (str, optional): absolute path to the persistent App state.
                If not provided, the one passed upon creation
                (see :any:`state_path`) will be used.
                The file should contain a json formatted as

                .. code-block:: json

                    {
                        "options": [
                            {
                                "text": "Option name",
                                "script": "script_name.sh"
                            }
                        ]
                    }

                Optional attributes for each `option` are:

                * ``installed`` (`int`): timestamp of script last run

        Returns:
            dict: parsed `public` options dictionary

        """
        if path:
            # store the new path if given
            self.state_path = path

        with click.open_file(self.state_path) as fo:
            #: Parsed data from the persistent stored file.
            self._state = json.load(fo)

        #: Private option sections, reflects exactly the options contained in
        #: the persistent state file
        self._options = self._state['options']
        #: Exposed options, can be modified at runtime to add or remove options
        #: from a CLI application
        self.options = copy.deepcopy(self._options)

        return self.options

    def save(self, path=None):
        """
        Dump the current ``_state`` attribute into the given path.

        Args:
            path (str, optional): absolute path to json file.
                If not provided the path provided on `init` will be used.
        """
        path = path or self.state_path
        with click.open_file(path, 'w', atomic=True) as fo:
            json.dump(self._state, fo, indent=4)

    # ##############################
    # Options handling
    # Functions to add and update options are in this group

    def add_option(self, text, callbackFn, idx=False, *args, **kwargs):
        """
        Add one option to the options for the app menu.
        If a `idx` is given, the item will be put at that position
        """
        def is_number():  # 0 is a position, but falsy
            return type(idx) is int

        def in_range():  # must be in range
            return idx >= 0 and idx < len(self.options)

        idx = idx if is_number() and in_range() else len(self.options)
        self.options.insert(idx, {
            'text': text,
            'callback': callbackFn,
        })

        # add extra option properties
        for k, v in kwargs.items():
            self.options[idx][k] = v

        return idx

    def update_option(self, name=None, idx=None, *args, **kwargs):
        """
        Update the `installed` attribute of the given option, either by
        `name` ('text' attribute) or by `idx` (index in the option list)
        """
        # Look up both private (in_options) and public (options) indexes
        # for the given option name or index. Note that they can result as
        # None if the passed name is wrong (both) or the option has been added
        # at runtime (private_idx)
        if name and not idx:
            public_idx = self.find_option_idx(name)
            private_idx = self._find_json_option_idx(name)
        elif idx and not name:
            public_idx = idx
            name = self.options[public_idx]['text']
            private_idx = self._find_json_option_idx(name)
        else:
            raise ValueError('Missing option <idx> or <text> values')

        install_date = arrow.now().timestamp  # get timestamp with arrow

        try:
            self.options[public_idx]['installed'] = install_date
        except (TypeError, IndexError) as e:
            # IndexError should never happen, but can be raised when accessing
            # the list. TypeError can be raised when public_idx is None due to
            # option not found. This should not happen, so reraise.
            msg = 'Option {} (`{}`) not found.'.format(public_idx, name)
            raise six.raise_from(IndexError(msg), e)

        try:
            self._options[private_idx]['installed'] = install_date
        except TypeError:
            # option added at runtime, so it can't be found in the private
            # options list. cases are that private_idx is None due to searching
            # for a non persistent option. we don't care about the case and
            # fail silently.
            pass

        # dump the updated private _options to the file.
        self.save()

    # ##############################
    # Options lookup

    def _find_option_idx(self, value, key, option_attr):
        """
        Find an option index inside the `option_attr` dictionary,
        checking the given ``key`` attribute of each option against the
        given ``value``.

        Returns:
            ``int`` if option is found, ``None`` otherwise.
        """
        for i, v in enumerate(option_attr):
            if v.get(key, '').lower() == value.lower():
                return i
        return None

    def find_option_idx(self, value, key='text'):
        """
        Return an option index inside the app options using a key - value pair.
        """
        return self._find_option_idx(value, key, self.options)

    def _find_json_option_idx(self, value, key='text'):
        """
        Find the index of the option inside the stored unmodified data
        recovered by the state.json file.
        """
        return self._find_option_idx(value, key, self._options)
