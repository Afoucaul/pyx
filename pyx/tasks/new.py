"""Pyx project creation

Usage:
    new <name>
"""

import os
import docopt
import sys
import getpass
from pyx import utils as pyxutl
from pyx import errors as pyxerr



TEST_SKELETON = '''"""Unit tests for {app}
"""

import unittest

class Test{app}(unittest.TestCase):
    def test_the_truth(self):
        assert True
'''


SETUP_SKELETON = '''import setuptools


settings = {{
    'name':     "{project}",
    'version':  "1.0",
    'author':   "{user}"
}}

if __name__ == '__main__':
    setuptools.setup(**settings)
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


PROJECT_SKELETON = '''"""Project attributes

Add here all that you need to manage your project.
"""

# PyPI distrubution management.
# You can avoid typing your plain credentials here, by using keyring.
pypi = {{
    'username':      '',
    'password':      '',
    'repository':    'https://test.pypi.org/legacy'
}}
'''


ENTRY_POINT_SKELETON = '''"""main.py

Entry point for the project.
"""
import {package}


def main():
    print("Greetings from {package}!")


if __name__ == '__main__':
    main()
'''


def create_project(cwd, name):
    target = os.path.join(cwd, name)

    if not pyxutl.validate_project_name(name):
        raise pyxerr.PyxError("Name should match the following pattern: {}".format(
            pyxutl.VALID_NAME_PATTERN))

    if os.path.isdir(target):
        pyxutl.print_colors(
                "A {}/ directory already exists".format(name), 
                fg="RED",
                style="BRIGHT")
        raise pyxerr.TaskError()

    pyxutl.print_colors(
            "Creating project {}...".format(name),
            fg="GREEN",
            style="BRIGHT")

    pyxutl.mkdir(target)
    os.chdir(target)


def create_structure(name):
    pyxutl.mkdir("test")
    pyxutl.write_file(
            os.path.join("test", "test_{}.py".format(name)),
            TEST_SKELETON.format(app=pyxutl.underscores_to_camel(name)))

    pyxutl.write_file(
            ".gitignore",
            "# Write here what you want to ignore")

    pyxutl.write_file(
            "main.py",
            ENTRY_POINT_SKELETON.format(package=name))

    pyxutl.write_file(
            "README.md",
            "# {}".format(name))

    pyxutl.write_file(
            "setup.py",
            SETUP_SKELETON.format(
            project=name, user=getpass.getuser()))

    pyxutl.mkdir(name)
    pyxutl.write_file(
            os.path.join(name, "__init__.py"),
            "from importlib import import_module")

    pyxutl.mkdir(".pyx")
    pyxutl.write_file(
            os.path.join(".pyx", "project.py"),
            PROJECT_SKELETON.format(package=name))
    pyxutl.mkdir(os.path.join(".pyx", "tasks"))


def init_pipenv():
    try:
        from pipenv import core as pc
        pc.ensure_project()
    except ImportError:
        message = "pipenv is not available, "
        try:
            import pip
            message += "do you wish to install it with pip?"
            if pyxutl.prompt(message):
                pip.main(["install", "pipenv"])
                from pipenv import core as pc
                pc.ensure_project()
            else:
                pyxutl.print_warning("pipenv not found, skipping pipenv initialization")
        except ImportError:
            message += "nor is pip. Skipping pipenv initialization"
            pyxutl.print_warning(message)


def main():
    args = docopt.docopt(__doc__)

    name = args['<name>']
    cwd = os.getcwd()
    create_project(cwd, name)
    create_structure(name)
    init_pipenv()


if __name__ == '__main__':
    main()
