"""Run tests in a Pyx project.

Usage: 
    pyx test
"""

import os
import pyx
import unittest



class PyxTaskTest(pyx.Task):
    def run(self):
        os.system("python3 -m unittest -v")
