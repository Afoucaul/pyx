"""Run tests in a Pyx project.

Usage: 
    pyx test
"""

import pyx
import unittest
import glob
import os


class PyxTaskTest(pyx.Task):
    def run(self):
        unittest.main(module=None)
