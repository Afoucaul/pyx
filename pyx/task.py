import os


class TaskFailure(Exception):
    def __init__(self, origin):
        super().__init__("Task {} aborted.".format(origin))


class Task:
    """Base class for tasks"""
    def __init__(self, cwd, *env):
        self.cwd = cwd
        self.env = env

    def run(self):
        raise NotImplementedError

    def fail(self):
        raise TaskFailure(type(self).__module__)
