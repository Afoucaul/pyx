import importlib
import os


def load_module(path, module_name):
    """Load a module given its path, and loads it and returns it"""
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def mkdir(path):
    try:
        os.mkdir(path)
        print("Created directory {}".format(path))

    except FileExistsError:
        print("Skipped creation of directory {}".format(path))


def write_file(path, content):
    try:
        open(path, 'r').close()
        print("Skipping writing of file {}".format(path))

    except FileNotFoundError:
        with open(path, 'w') as file:
            file.write(content)
        print("Created file {}".format(path))
