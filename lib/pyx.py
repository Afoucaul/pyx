class Task:
    def __init__(self, env):
        self.env = env

    def run(self):
        raise NotImplementedError
