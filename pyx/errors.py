class PyxError(Exception):
    pass

class TaskError(Exception):
    pass

class ConfigError(Exception):
    def __init__(self, config, attr):
        super().__init__("{} config has no {} attribute".format(config.name, attr))
