import importlib
import os
import sys
import enum
import re
try:
    import colorama
    colorama.init()
except ImportError:
    print(
            "Module colorama was not found; "
            "you can install it with `pip3 install colorama`", 
            file=sys.stderr)
    colorama = None
from . import errors as pyxerr
from . import tasks


VALID_NAME_PATTERN = r'^[a-z][a-z0-9_]*$'


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


def print_error(*args, **kwargs):
    print_colors("E -", *args, fg="RED", style="BRIGHT", file=sys.stderr, **kwargs)


def print_warning(*args, **kwargs):
    print_colors("W -", *args, fg="RED", style="NORMAL", file=sys.stderr, **kwargs)


def print_info(*args, **kwargs):
    print_colors(*args, fg="GREEN", style="NORMAL")


def print_success(*args, **kwargs):
    print_colors(*args, fg="GREEN", style="BRIGHT")


def print_list(l):
    l = list(l)
    label_width = max(len(x) for x, _ in l)
    for label, text in l:
        print_colors(
                "  {label: <{width}}    ".format(label=label, width=label_width),
                fg="BLUE", style="BRIGHT", end="")
        print(text)

def prompt(message):
    while True:
        print_colors("{} [Y]es/[N]o".format(message), fg="BLUE")
        result = input("> ")
        if result in ('y', 'yes'):
            return True
        elif result in ('n', 'no'):
            return False


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


def validate_project_name(name):
    return re.match(VALID_NAME_PATTERN, name)


def underscores_to_camel(name):
    return name.replace('_', ' ').title().replace(' ', '')


def ensure_pyx():
    if not os.path.isdir(".pyx"):
        print_error("No .pyx/ directory found. Please run this inside a pyx project.")
        sys.exit(1)


def get_project():
    return load_module(os.path.join(os.getcwd(), ".pyx", "project.py"), "project")


def get_settings():
    return load_module("setup.py", "setup").settings


def is_git():
    return os.path.isdir(".git")


def get_tasks():
    tasks_dict = {}

    global_root = os.path.dirname(os.path.abspath(tasks.__file__))
    files = os.listdir(global_root)
    for f in files:
        if not f.endswith(".py") or f == "__init__.py":
            continue
        shortdoc = load_module(os.path.join(global_root, f), f[:-3]).__doc__.split('\n')[0]
        tasks_dict[f[:-3]] = shortdoc

    local_root = os.path.join(os.getcwd(), ".pyx", "tasks")
    files = os.listdir(local_root)
    for f in files:
        if not f.endswith(".py") or f == "__init__.py":
            continue
        shortdoc = load_module(os.path.join(local_root, f), f[:-3]).__doc__.split('\n')[0]
        tasks_dict[f[:-3]] = shortdoc

    return tasks_dict.items()
