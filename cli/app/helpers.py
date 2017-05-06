"""
Helper classes for composing the main AppManager object
"""


class OptionsManager(object):
    """
    An OptionsManager object handles and keep track of both the persistent
    app state and the runtime options and state, such as options structure,
    installation status etc and takes care of handling reading and saving on
    the persistent app state.
    """
    pass


class ScriptParser(object):
    """
    Takes care of parsing a script file for the various informations that may
    be required to setup both the runtime options and the CLI visualization,
    such as script title, description, parsing description `click` metadata
    (text weight, color, etc).
    """

    # marker for script title inside the scripts
    OPT_TITLE = '#!title: '
    # delimiters for the script description paragraph
    OPT_DESCR_IN = '#!description'
    OPT_DESCR_OUT = '#!end-description'
    # if present the app wil ignore the script for what concerns options and direct
    # execution. script can still be used from other script or directly, os this
    # can be useful for utility scripts, tests or work in progress
    OPT_SKIP = '#!~SKIP'
    # if present the app will store the script data inside the persistent state
    OPT_SAVE = '#!~SAVE'


class Config(object):
    """
    Config takes care of handling basic configuration such as paths to folders
    and files, verbosity and other stuff that can be configured either by
    environment variables or by the application itself (or cli) to change some
    behaviour.
    """

    def __init__(self, ctx):
        # Application context
        self.ctx = ctx
        self._verbose = 0

    @property
    def verbosity(self):
        return self._verbose

    @verbosity.setter
    def verbosity(self, v):
        # This should set the proper Logger verbosity value depending on the
        # Int value passed. for now this mock will do.
        self._verbose = v
