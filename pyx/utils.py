import importlib
import os
import sys
import enum
try:
    import colorama
    colorama.init()
except ImportError:
    print(
            "Module colorama was not found; "
            "you can install it with `pip3 install colorama`", 
            file=sys.stderr)
    colorama = None


def print_colors(*args, bg="RESET", fg="RESET", style="NORMAL", **kwargs):
    if colorama is not None: 
        args = ["{}{}{}{}{}".format(
            getattr(colorama.Back, bg), 
            getattr(colorama.Fore, fg), 
            getattr(colorama.Style, style), 
            arg, 
            colorama.Style.RESET_ALL) 
            for arg in args]
    print(*args, **kwargs)


def load_module(path, module_name):
    """Load a module given its path, and loads it and returns it"""
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def mkdir(path):
    try:
        os.mkdir(path)
        print_colors("Created directory {}".format(path), fg="GREEN")

    except FileExistsError:
        print_colors("Skipped creation of directory {}".format(path), fg="RED")


def write_file(path, content):
    try:
        open(path, 'r').close()
        print_colors("Skipped writing of file {}".format(path), fg="RED")

    except FileNotFoundError:
        with open(path, 'w') as file:
            file.write(content)
        print_colors("Created file {}".format(path), fg="GREEN")
