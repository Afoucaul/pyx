import os
import importlib


class Task:
    def run(self):
        raise NotImplementedError


class Config:
    def __init__(self):
        pass

    @classmethod
    def get(cls):
        config_path = os.path.join(os.getcwd(), "pyx_config.py")

        config_spec = importlib.util.spec_from_file_location("pyx_config", config_path)
        config_module = importlib.util.module_from_spec(config_spec)
        config_spec.loader.exec_module(config_module)

        for attr in config_module.__dict__.values():
            if isinstance(attr, type) and issubclass(attr, cls):
                return attr

        raise Exception("No config found")
