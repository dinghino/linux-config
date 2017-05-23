# -*- coding: utf-8 -*-
import importlib
import os
import site

import pip
import six

cwd = os.path.dirname(__file__)
reqfp = os.path.join(cwd, 'requirements.txt')
with open(reqfp) as fo:
    requirements = fo.read().split('\n')
    if requirements[-1] == '':  # last could be a newline char. check and remove
        requirements = requirements[:-1]


def install_if_not_found(package):
    try:
        importlib.import_module(package)
        six.print_('= %s ok...' % package)
    except ImportError:
        six.print_('- %s not found.  installing...')
        pip.main(['install', package, '-no-cache-dir'])
        six.print_('+ installed.')
        # update packages cache
        reload(site)  # noqa: F821
    finally:
        globals()[package] = importlib.import_module(package)


for package in requirements:
    install_if_not_found(package.split('==')[0])


# Execute the program
from cli import cli  # noqa: E402
cli()
