# -*- coding: utf-8 -*-
import os


class ScriptParser(object):
    """
    Takes care of parsing a script file for the various informations that may
    be required to setup both the runtime options and the CLI visualization,
    such as script title, description, parsing description `click` metadata
    (text weight, color, etc).

    Arguments:
        ctx (:any:`AppManager`): Application manager context.

    """

    #: marker for script title inside the scripts
    OPT_TITLE = '#!title: '
    #: Delimit the start of a description paragraph
    OPT_DESCR_IN = '#!description'
    #: Delimit the end of the description paragraph
    OPT_DESCR_OUT = '#!end-description'
    #: if present the app wil ignore the script for what concerns options and
    #: direct execution. script can still be used from other script or
    #: directly, os this can be useful for utility scripts, tests or work
    #: in progress
    OPT_SKIP = '#!~SKIP'
    #: if present the app will save the script data inside the persistent state
    OPT_SAVE = '#!~SAVE'

    def __init__(self, ctx):
        self.ctx = ctx

    def parse_scripts_folder(self, folder_name, state):
        """
        Walk the given `folder_name` and parse every ``.sh`` file found inside

        Args:
            folder_name (str): Absolute path pointing to the folder containing
                the scripts to parse.

            state (:any:`StateManager`): StateManager instance to load the
                parsed options into.

        """
        def abspath(fn):
            return os.path.join(folder_name, fn)

        def is_file(fn):
            return os.path.isfile(abspath(fn))

        filenames = os.listdir(folder_name)
        # get a list of absolute path to the files inside self.scripts_dir if
        # the file ends with .sh - assume it's a bash script
        scripts = [
            abspath(fn) for fn in filenames
            if is_file(fn) and fn.endswith('.sh')
        ]

        for i, script in enumerate(scripts):
            title, description, path, skip = self.parse_script_metadata(
                script)
            if skip:
                continue

            def opt_callback():
                return self.ctx.execute(path)

            state.add_option(title, opt_callback, i,
                             description=description)

    def parse_script_metadata(self, filepath):
        """
        Read a script file from a < filepath > and extract all the commented
        lines

        Args:
            filepath (str): absolute path to the file to parse.

        Returns:
            tuple:

                * title (`str`): Script title
                * description (`str`): Summary description
                * script_path (`str`): Asbolute path to the script file
                * skip (`bool`): wether the script should be skipped for
                  options and other application functionalities
                  (i.e. an utils.sh)
        """

        # TODO: Use this and process_scripts_folder to process the scripts and
        # automatically generate and update state.json with currently available
        # scripts.
        # The function should remove options that don't have the script
        # available and add the new options found.
        # All the scripts will have to contain some sort of header that will
        # describe the option TEXT and other metainformation that could be
        # useful (i.e. desired options list position, text color etc...)

        title = 'No Title'
        description = 'No Description available'
        skip = False

        def get_title(line):
            return line.strip().split('#!title: ')[1]

        with open(filepath) as fo:
            is_description = False
            for line in fo:
                if line.startswith(self.OPT_SKIP):
                    # If the line starts with the SKIP shebang the script will
                    # be set to be skipped in further processing and the loop
                    # will stop (useless parse more data since we won't use it)
                    skip = True
                    break

                # When true the loop will stop to parse the description
                if line.startswith(self.OPT_DESCR_OUT):
                    is_description = False

                if is_description:
                    try:
                        description += line.split('# ', 1)[1]
                    except IndexError:  # Blank line
                        description += '\n'
                    continue

                if line.startswith(self.OPT_TITLE):
                    title = get_title(line)

                elif line.startswith(self.OPT_DESCR_IN):
                    # When true the loop will start to parse the description
                    is_description = True
                    description = ''

        return (title, description.strip(), filepath, skip)
