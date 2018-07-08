"""Pyx project creation

Usage:
    pyx new <name>
"""

import pyx
import os
import re


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


def validate_name(name):
    assert re.match(r'^[a-z][a-z0-9_]*$', name)


def underscores_to_camel(name):
    return name.replace('_', ' ').title().replace(' ', '')


class PyxTaskNew(pyx.Task):
    def __init__(self, cwd, name):
        self.cwd = cwd
        validate_name(name)
        self.name = name

        self.target = os.path.join(self.cwd, self.name)

    def run(self):
        pyx.utils.mkdir(self.target)
        os.chdir(self.target)
        self._create_skeleton()

    def _create_skeleton(self):
        self._create_test()
        self._create_lib()
        self._create_gitignore()
        self._create_readme()
        self._create_app()
        self._create_config()

    def _create_test(self):
        pyx.utils.mkdir("test")
        pyx.utils.write_file(
                os.path.join("test", "test_{}.py".format(self.name)),
                TEST_SKELETON.format(app=underscores_to_camel(self.name)))

    def _create_lib(self):
        pyx.utils.mkdir(self.name)
        with open(os.path.join(self.name, "__init__.py"), 'w'):
            pass

    def _create_gitignore(self):
        pyx.utils.write_file(
                ".gitignore",
                "# Write here what you want to ignore")

    def _create_readme(self):
        pyx.utils.write_file(
                "README.md",
                "# {}".format(self.name))

    def _create_app(self):
        pyx.utils.write_file(
                "pyx_app.py",
                APP_SKELETON.format(
                module=self.name, app=underscores_to_camel(self.name)))

    def _create_config(self):
        pyx.utils.mkdir("config")
        pyx.utils.write_file(
                os.path.join("config", "default.py"),
                CONFIG_SKELETON)
