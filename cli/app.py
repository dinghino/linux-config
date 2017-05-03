# -*- coding: utf-8 -*-
"""
Application manager.
"""
import copy
import json
import os
import shlex
import six
import subprocess
import time
from datetime import datetime

import click

APP_FOLDER_NAME = 'cli'


class AppManager(object):
    """
    Context and Configuration variables for the application.
    """

    def __init__(self):
        # absolute path of the python application
        self._app_dir = os.path.dirname(__file__)
        # absolute path to the root folder of the application. Uses os.path
        # instead of pathlib to try and mantain python 2.7 compatibility.
        # this file is in <root>/cli/ so we need to walk up one
        self._root_dir = os.path.dirname(self._app_dir)
        # folder where the scripts are
        self.scripts_dir = os.path.join(self._root_dir, 'scripts')
        # path to the app state file (state.json)
        self._app_state_path = os.path.join(self._app_dir, 'state.json')
        # verbosity level, for logging and stuff
        self.verbose = 0
        # root of the project, so the program can access files
        self.root = '.'
        # sudo password, so it can be used automatically
        self.sudo = None
        # wether the setup has been done or not
        self.setup_done = False
        # state of the application functionalities, used to generate menu
        # and do callbacks.
        # self._options is exactly the data stored in the json, that have to
        # be kept as it is and updated only with serializable key-values,
        # while the public `options` can be worked on at runtime
        # (setting callback functions, adding other options etc...)
        with click.open_file(self._app_state_path) as fo:
            self._options = json.load(fo)
            self.options = copy.deepcopy(self._options)

        # setup the callbacks
        for opt in self.options:
            opt['callback'] = self._generate_callback(opt)

    def get_script_path(self, filename):
        """
        Return the absolute path to the script file inside the scripts folder.
        """
        return os.path.join(self.scripts_dir, filename)

    def execute(self, script, cb=lambda: None, *args, **kwargs):
        """
        Execute the given script, then call the optional callback passing
        the script output as first argument and all extra arguments given.
        """
        # NOTE: For now assume the the <script> argument is a path to valid
        # script and try to call it. Later we'll check if it's a path, if it
        # points to something (exists), otherwise we'll assume that it's the
        # script's name and try to evaluate its path.
        _execute = shlex.split(script)
        p = subprocess.Popen(_execute, stdout=subprocess.PIPE)
        output, error = p.communicate()
        output = output.decode('utf-8')
        try:
            cb(result=output, *args, **kwargs)
        except TypeError:  # not callable, maybe?
            pass
        return output

    def _generate_callback(self, opt):
        """
        Generate a callback function for the app options from parameters
        recovered from the json storing the state.
        """
        label = 'Processing callback for {}'.format(opt.get('script'))

        def cb(*args, **kwargs):
            with click.progressbar(range(5), label=label) as bar:
                for i_ in bar:
                    time.sleep(.63)

            self.update_option(opt['text'])

        return cb

    def add_option(self, text, callback, idx=False, *args, **kwargs):
        """
        Add one option to the options for the app menu.
        If a `idx` is given, the item will be put at that position
        """
        def is_number():  # 0 is a position, but falsy
            return type(idx) is int

        def in_range():  # must be in range
            return idx >= 0 and idx < len(self.options)

        idx = idx if is_number() and in_range() else len(self.options)
        self.options.insert(idx, {'text': text, 'callback': callback})

        # add extra option properties
        for k, v in kwargs.items():
            self.options[idx][k] = v

        return idx

    def find_option_idx(self, value, key='text'):
        """
        Return an option index inside the app options using a key-value pair.
        """
        return self._find_option_idx(value, key, self.options)

    def _find_json_option_idx(self, value, key='text'):
        """
        Find the index of the option inside the stored unmodified data recovered
        by the state.json file.
        """
        return self._find_option_idx(value, key, self._options)

    def _find_option_idx(self, value, key, option_attr):
        """Find an option index. """
        for i, v in enumerate(option_attr):
            if v.get(key, '').lower() == value.lower():
                return i
        return None

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

        install_date = datetime.now().strftime('%d/%m/%Y')

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
        with click.open_file(self._app_state_path, 'w', atomic=True) as fo:
            json.dump(self._options, fo, indent=4)
