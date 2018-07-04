"""Pyx project creation

Usage:
    pyx new <name>
"""

import pyx
import os


CONFIG_SKELETON = '''import pyx

class PyxConfigDefault(pyx.Config):
    environment = "dev"'''


APP_SKELETON = """import pyx

class {app}(pyx.Application):
    def __init__(self, config):
        super().__init__(config)

    def run(self):
        print("Greetings from {app}!")"""


TEST_SKELETON = """import unittest

class Test{app}(unittest.TestCase):
    def test_the_truth(self):
        assert True
"""


class PyxTaskNew(pyx.Task):
    def __init__(self, cwd, name):
        self.cwd = cwd
        self.name = name

        self.target = os.path.join(self.cwd, self.name)

    def run(self):
        os.mkdir(self.target)
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
        os.mkdir("test")
        with open("test/test_{}.py".format(self.name), 'w') as test:
            test.write(TEST_SKELETON.format(app=self.name.capitalize()))

    def _create_lib(self):
        os.mkdir("lib")

    def _create_gitignore(self):
        with open(".gitignore", 'w') as gitignore:
            gitignore.write("# Write here what you want to ignore")

    def _create_readme(self):
        with open("README.md", 'w') as readme:
            readme.write("# {}".format(self.name))

    def _create_app(self):
        with open("pyx_app.py", 'w') as app:
            app.write(APP_SKELETON.format(app=self.name.capitalize()))

    def _create_config(self):
        os.mkdir("config")
        with open(os.path.join("config", "default.py"), 'w') as default_config:
            default_config.write(CONFIG_SKELETON)
