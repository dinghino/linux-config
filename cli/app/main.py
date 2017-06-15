# -*- coding: utf-8 -*-
"""
Application manager.
Takes care of running scripts correctly, keeping track of paths and of the
application state through persistent data.
"""
import shlex
import subprocess
import time  # used for temporary callback on _generate_callback

import click

from .helpers import ScriptParser, Config, StateManager


class AppManager(object):
    """
    Context and Configuration variables for the application.

    Arguments:
        config (:any:`Config`): Configuration object
        parser (:any:`ScriptParser`): Parsing helper class
    """

    def __init__(self):
        # Configuration object
        self.config = Config(self)
        # Parser for script files
        self.parser = ScriptParser(self)
        # Application state manager
        # Used to handle the persistent state file, get the options dict to
        # generate menu.
        # self.options is exactly the data stored in the json, that have to
        # be kept as it is and updated only with serializable key-values,
        # `public` .options, isexposed for client purposes but that won't be
        # saved on the persistent storage and can be worked on at runtime
        # (setting callback functions, adding other options etc...)
        self.state = StateManager(self, self.config.state_path)

        # setup the callbacks
        for opt in self.state.options:
            opt['callback'] = self._generate_callback(opt)

        self.parser.parse_scripts_folder(self.config.scripts_dir, self.state)

    @property
    def verbosity(self):
        return self.config.verbosity

    @verbosity.setter
    def verbosity(self, value):
        self.config.verbosity = value

    @property
    def options(self):
        return self.state.options

    def execute(self, script, cb=lambda: None, *args, **kwargs):
        """
        Execute the given script, then call the optional callback passing
        the script output as first argument and all extra arguments given.
        """
        # TODO: For now assume the the <script> argument is a path to valid
        # script - or a shell command - and try to call it. Later
        # we may want to check if it's a path, if it points to something,
        # has some kind of flag for a shell command, or otherwise
        # assume that it's the script's name and try to evaluate its path.
        _execute = shlex.split(script)

        p = subprocess.Popen(
            _execute, shell=True, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, error = p.communicate()
        output = output.decode('utf-8')
        error = error.decode('utf-8')

        try:
            cb(result=output, *args, **kwargs)
        except TypeError:  # not callable, maybe?
            pass
        return output, error

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

            self.state.update_option(opt['text'])

        return cb
