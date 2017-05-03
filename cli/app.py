"""
Application manager.
"""
import json
import os
import time
from datetime import datetime

import click


class AppManager(object):
    """
    Context and Configuration variables for the application.
    """

    def __init__(self):
        # verbosity level, for logging and stuff
        self.verbose = 0
        # root of the project, so the program can access files
        self.root = '.'
        # sudo password, so it can be used automatically
        self.sudo = None
        # wether the setup has been done or not
        self.setup_done = False
        # state of the application functionalities, used to generate menu
        # and do callbacks
        with open(os.path.join(os.path.dirname(__file__), 'state.json')) as fo:
            self.options = json.load(fo)
        # setup the callbacks
        for opt in self.options:
            opt['callback'] = self._generate_callback(opt)

    def _generate_callback(self, opt):
        """
        Generate a callback function for the app options from parameters
        recovered from the json storing the state.
        """
        label = 'Processing callback for {}'.format(opt['callback'])

        def cb(*args, **kwargs):
            with click.progressbar(range(5), label=label) as bar:
                for i_ in bar:
                    time.sleep(.63)

            self.update_option(opt['text'])

        return cb

    def add_option(self, text, callback, pos=False, *args, **kwargs):
        """
        Add one option to the options for the app menu.
        If a `pos` is given, the item will be put at that position
        """
        def is_number():  # 0 is a position, but falsy
            return type(pos) is int

        def in_range():  # must be in range
            return pos >= 0 and pos < len(self.options)

        idx = pos if is_number() and in_range() else len(self.options)
        self.options.insert(idx, {'text': text, 'callback': callback})

        # add extra options
        for k, v in kwargs.items():
            self.options[idx][k] = v

        return idx

    def find_option_idx(self, value, key='text'):
        """Find an option index. """
        for i, v in enumerate(self.options):
            try:
                value = value.lower()
            except AttributeError:
                pass

            if v.get(key, '').lower() == value:
                return i
        return None

    def update_option(self,  name=None, idx=None, value=None, *args, **kwargs):
        """
        Update the `installed` attribute of the given option, either by
        `name` ('text' attribute) or by `idx` (index in the option list)
        """
        if not name and not idx:
            raise ValueError('Missing option <idx> or <text> values')
        if name and not idx:
            idx = self.find_option_idx(name)

        value = value or datetime.now().strftime('%d/%m/%Y')
        self.options[idx]['installed'] = value
