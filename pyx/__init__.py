from importlib import import_module

name = "pyx"

utils = import_module(".utils", __name__)
errors = import_module(".errors", __name__)
application = import_module(".application", __name__)
config = import_module(".config", __name__)

Application = application.Application
Config = config.Config
