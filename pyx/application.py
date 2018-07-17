import os
from .utils import load_module

class Application:
    """Base class for application"""
    def __init__(self, config):
        self.config = config

    def run(self):
        raise NotImplementedError

    @classmethod
    def get(cls):
        app_path = os.path.join(os.getcwd(), ".pyx", "app.py")
        app_module = load_module(app_path, "pyx_app")

        for attr in app_module.__dict__.values():
            if isinstance(attr, type) and issubclass(attr, cls):
                return attr

        raise Exception("No app found")
