import os
import importlib


class Task:
    """Base class for tasks"""
    def __init__(self, cwd, *env):
        self.cwd = cwd
        self.env = env

    def run(self):
        raise NotImplementedError


class Config:
    """Base class for project configs"""
    @classmethod
    def get(cls, name):
        config_path = os.path.join(os.getcwd(), "config", name + ".py")
        config_module = load_module(config_path, "config")

        for attr in config_module.__dict__.values():
            if isinstance(attr, type) and issubclass(attr, cls):
                return attr

        raise Exception("No config found")


class Application:
    """Base class for application"""
    def __init__(self, config):
        self.config = config

    def run(self):
        raise NotImplementedError

    @classmethod
    def get(cls):
        app_path = os.path.join(os.getcwd(), "pyx_app.py")
        app_module = load_module(app_path, "pyx_app")

        for attr in app_module.__dict__.values():
            if isinstance(attr, type) and issubclass(attr, cls):
                return attr

        raise Exception("No app found")


def load_module(path, module_name):
    """Load a module given its path, and loads it and returns it"""
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module
