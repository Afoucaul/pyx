"""Pyx project creation

Usage:
    new <name>
"""

import os
import re
import docopt
import sys


CONFIG_SKELETON = '''import pyx

class PyxConfigDefault(pyx.Config):
    environment = "dev"'''


APP_SKELETON = """import pyx
import {module}

class {app}App(pyx.Application):
    def __init__(self, config):
        super().__init__(config)

    def run(self):
        print("Greetings from {app}!")"""


TEST_SKELETON = """import unittest

class Test{app}(unittest.TestCase):
    def test_the_truth(self):
        assert True
"""


SETUP_SKELETON = """import setuptools

setuptools.setup(
    name="{project}",
    version="1.0"
)
"""

VALID_NAME_PATTERN = r'^[a-z][a-z0-9_]*$'


def validate_name(name):
    return re.match(VALID_NAME_PATTERN, name)


def underscores_to_camel(name):
    return name.replace('_', ' ').title().replace(' ', '')


class PyxTaskNew():
    def __init__(self, cwd, name):
        self.cwd = cwd
        self.name = name
        self.target = os.path.join(self.cwd, self.name)

    def run(self):
        if not validate_name(self.name):
            raise Exception("Name should match the following pattern: {}".format(
                VALID_NAME_PATTERN))

        if os.path.isdir(self.target):
            pyx.utils.print_colors(
                    "A {}/ directory already exists".format(self.name), 
                    fg="RED",
                    style="BRIGHT")
            self.fail()

        pyx.utils.print_colors(
                "Creating project {}...".format(self.name),
                fg="GREEN",
                style="BRIGHT")

        pyx.utils.mkdir(self.target)
        os.chdir(self.target)
        self._create_skeleton()

    def _create_skeleton(self):
        self._create_test()
        self._create_lib()
        self._create_setup()
        self._create_gitignore()
        self._create_readme()
        self._create_pyx()
        self._create_app()
        self._create_config()
        self._init_pipenv()

    def _create_test(self):
        pyx.utils.mkdir("test")
        pyx.utils.write_file(
                os.path.join("test", "test_{}.py".format(self.name)),
                TEST_SKELETON.format(app=underscores_to_camel(self.name)))

    def _create_pyx(self):
        pyx.utils.mkdir(".pyx")

    def _create_gitignore(self):
        pyx.utils.write_file(
                ".gitignore",
                "# Write here what you want to ignore")

    def _create_readme(self):
        pyx.utils.write_file(
                "README.md",
                "# {}".format(self.name))

    def _create_lib(self):
        pyx.utils.mkdir(self.name)
        with open(os.path.join(self.name, "__init__.py"), 'w'):
            pass

    def _create_app(self):
        pyx.utils.write_file(
                os.path.join(".pyx", "app.py"),
                APP_SKELETON.format(
                module=self.name, app=underscores_to_camel(self.name)))

    def _create_setup(self):
        pyx.utils.write_file(
                os.path.join(self.name, "setup.py"),
                SETUP_SKELETON.format(
                project=self.name))

    def _create_config(self):
        pyx.utils.mkdir(os.path.join(".pyx", "config"))
        pyx.utils.write_file(
                os.path.join(".pyx", "config", "default.py"),
                CONFIG_SKELETON)

    def _init_pipenv(self):
        try:
            from pipenv import core as pc
            pc.ensure_project()
        except ImportError:
            message = "pipenv is not available, "
            try:
                import pip
                message += "do you wish to install it with pip?"
                if pyx.utils.prompt(message):
                    os.system("pip3 install pipenv")
                    from pipenv import core as pc
                    pc.ensure_project()
                else:
                    pyx.utils.print_warning("pipenv not found, skipping pipenv initialization")
            except ImportError:
                message += "nor is pip. Skipping pipenv initialization"
                pyx.utils.print_warning(message)


def main(args):
    name = args['<name>']
    cwd = os.getcwd()
    write_skeleton(cwd, name)


if __name__ == '__main__':
    print(sys.argv)
    args = docopt.docopt(__doc__)
    main(args)
