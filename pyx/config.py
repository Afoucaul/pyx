import os
from .utils import load_module

class Config:
    """Base class for project configs"""
    @classmethod
    def get(cls, name):
        config_path = os.path.join(os.getcwd(), ".pyx", "config", name + ".py")
        config_module = load_module(config_path, "config")

        for attr in config_module.__dict__.values():
            if isinstance(attr, type) and issubclass(attr, cls):
                return attr

        raise Exception("No config found")
