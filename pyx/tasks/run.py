"""Pyx project execution

Usage:
    pyx run [<config>]
"""


import pyx
import os


class PyxTaskRun(pyx.Task):
    def __init__(self, cwd, config="default"):
        self.cwd = cwd
        self.app = pyx.Application.get()
        self.config = pyx.Config.get(config)

    def run(self):
        self.app(self.config).run()
