# -*- coding: utf-8 -*-
import os


class Config(object):
    """
    Config takes care of handling basic configuration such as paths to folders
    and files, verbosity and other stuff that can be configured either by
    environment variables or by the application itself (or cli) to change some
    behaviour.

    Arguments:
        ctx (:any:`AppManager`): Application manager context.

    Attributes:
        APP_FOLDER_NAME (str): Name of the application folder
        APP_STATE_FILENAME (str): Name of the file where all the persistent
            data is stored. default location is inside the `app/` folder.
        SCRIPTS_FOLDER (str): Name of the folder that contains the scripts run
            by the application. Path is relative to the project root.

        app_dir (str): absolute path to the python application folder
        root_dir (str): absolute path to the root of the whole program
        scripts_dir (str): absolute path to the scripts folder
            (see :any:`SCRIPTS_FOLDER`)
        state_path (str): absolute path to the persistent state file

    """
    APP_FOLDER_NAME = 'cli'
    APP_STATE_FILENAME = 'state.json'
    SCRIPTS_FOLDER = 'scripts'

    def __init__(self, ctx, verbose=0,
                 app_name=None, state_filename=None, scripts_folder=None):
        # Application context
        self.ctx = ctx
        self._verbose = verbose

        app_name = app_name or Config.APP_FOLDER_NAME
        state_filename = state_filename or Config.APP_STATE_FILENAME
        scripts_folder = scripts_folder or Config.SCRIPTS_FOLDER

        # Absolute path of the python application
        self.app_dir = os.path.abspath(
            os.path.dirname(os.path.dirname(__file__)))
        # Absolute path to the root folder of the application. Uses os.path
        # instead of pathlib to try and mantain python 2.7 compatibility.
        # this file is in <root>/cli/ so we need to walk up one
        self.root_dir = os.path.dirname(os.path.dirname(self.app_dir))
        # Folder where the scripts are
        self.scripts_dir = os.path.join(self.root_dir, scripts_folder)
        # Path to the app state file (state.json)
        self.state_path = os.path.join(self.app_dir, state_filename)

    @property
    def verbosity(self):
        """
        Property `verbose` is used to read or set the verbosity level of the
        application logging experience.
        """
        return self._verbose

    @verbosity.setter
    def verbosity(self, v):
        # This should set the proper Logger verbosity value depending on the
        # Int value passed. for now this mock will do.
        self._verbose = v
