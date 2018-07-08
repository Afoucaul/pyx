class Task:
    """Base class for tasks"""
    def __init__(self, cwd, *env):
        self.cwd = cwd
        self.env = env

    def run(self):
        raise NotImplementedError
