import os
import importlib


class Task:
    def run(self):
        raise NotImplementedError


class Config:
    @classmethod
    def get(cls, name):
        config_path = os.path.join(os.getcwd(), "config", name + ".py")

        config_spec = importlib.util.spec_from_file_location("pyx_config", config_path)
        config_module = importlib.util.module_from_spec(config_spec)
        config_spec.loader.exec_module(config_module)

        for attr in config_module.__dict__.values():
            if isinstance(attr, type) and issubclass(attr, cls):
                return attr

        raise Exception("No config found")


class Application:
    def __init__(self, config):
        self.config = config

    def run(self):
        raise NotImplementedError

    @classmethod
    def get(cls):
        app_path = os.path.join(os.getcwd(), "pyx_app.py")

        app_spec = importlib.util.spec_from_file_location("pyx_app", app_path)
        app_module = importlib.util.module_from_spec(app_spec)
        app_spec.loader.exec_module(app_module)

        for attr in app_module.__dict__.values():
            if isinstance(attr, type) and issubclass(attr, cls):
                return attr

        raise Exception("No app found")
