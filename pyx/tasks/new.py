"""Pyx project creation

Usage:
    new <name>
"""

import os
import docopt
import sys
from pyx import utils, errors


CONFIG_SKELETON = '''import pyx

class PyxConfigDefault(pyx.Config):
    environment = "dev"'''


APP_SKELETON = '''"""{app} pyx application

This script is the entry point for the pyx run command.
"""

import pyx
import {module}

class {app}App(pyx.Application):
    def __init__(self, config):
        super().__init__(config)

    def run(self):
        print("Greetings from {app}!")'''


TEST_SKELETON = '''"""Unit tests for {app}
"""

import unittest

class Test{app}(unittest.TestCase):
    def test_the_truth(self):
        assert True
'''


SETUP_SKELETON = '''import setuptools

setuptools.setup(
    name="{project}",
    version="1.0"
)
'''


MAIN_SKELETON = '''"""Package entry point

Usage:
    python -m package [<args>...]
"""

def main(args):
    print("Hello from pyx app")

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    main(args)
'''


def create_project(cwd, name):
    target = os.path.join(cwd, name)

    if not utils.validate_project_name(name):
        raise errors.PyxError("Name should match the following pattern: {}".format(
            utils.VALID_NAME_PATTERN))

    if os.path.isdir(target):
        utils.print_colors(
                "A {}/ directory already exists".format(name), 
                fg="RED",
                style="BRIGHT")
        raise errors.TaskError()

    utils.print_colors(
            "Creating project {}...".format(name),
            fg="GREEN",
            style="BRIGHT")

    utils.mkdir(target)
    os.chdir(target)


def create_structure(name):
    utils.mkdir("test")
    utils.write_file(
            os.path.join("test", "test_{}.py".format(name)),
            TEST_SKELETON.format(app=utils.underscores_to_camel(name)))

    utils.mkdir(".pyx")

    utils.write_file(
            ".gitignore",
            "# Write here what you want to ignore")

    utils.write_file(
            "README.md",
            "# {}".format(name))

    utils.mkdir(name)
    utils.write_file(
            os.path.join(name, "__init__.py"),
            "from importlib import import_module")

    utils.write_file(
            os.path.join(".pyx", "app.py"),
            APP_SKELETON.format(
            module=name, app=utils.underscores_to_camel(name)))

    utils.write_file(
            "setup.py",
            SETUP_SKELETON.format(
            project=name))

    utils.mkdir(os.path.join(".pyx", "config"))
    utils.write_file(
            os.path.join(".pyx", "config", "default.py"),
            CONFIG_SKELETON)


def init_pipenv():
    try:
        from pipenv import core as pc
        pc.ensure_project()
    except ImportError:
        message = "pipenv is not available, "
        try:
            import pip
            message += "do you wish to install it with pip?"
            if pyx.utils.prompt(message):
                pip.main(["install", "pipenv"])
                from pipenv import core as pc
                pc.ensure_project()
            else:
                utils.print_warning("pipenv not found, skipping pipenv initialization")
        except ImportError:
            message += "nor is pip. Skipping pipenv initialization"
            utils.print_warning(message)


def main(args):
    name = args['<name>']
    cwd = os.getcwd()
    create_project(cwd, name)
    create_structure(name)
    init_pipenv()


if __name__ == '__main__':
    print(sys.argv)
    args = docopt.docopt(__doc__)
    main(args)
