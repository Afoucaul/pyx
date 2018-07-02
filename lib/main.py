#! /usr/bin/env python3

"""
The Python task-oriented project manager.

Usage:
    pyx <task>
"""

import docopt
import os
import inspect
import importlib

PYX_PATH = os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda: 0)))


def retrieve_pyx(module):
    for attr in module.__dict__.values():
        # This check should be enough; else, check module's path against PYX_PATH + pyx.py
        if hasattr(attr, "__name__") and attr.__name__ == "pyx":
            return attr


def retrieve_task(task_module, pyx_module):
    for attr in task_module.__dict__.values():
        if isinstance(attr, type) and issubclass(attr, pyx_module.Task):
            return attr


def execute_task_from_module(task_module, env):
    pyx_module = retrieve_pyx(task_module)
    task = retrieve_task(task_module, pyx_module)

    task(env).run()


def extract_env(args):
    return {}


def main(args):
    print("Running pyx from {}".format(PYX_PATH))

    spec = importlib.util.spec_from_file_location(
            args['<task>'], 
            os.path.join(PYX_PATH, "tasks", args['<task>'] + ".py"))
    task_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(task_module)

    env = extract_env(args)
    execute_task_from_module(task_module, env)
    

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    main(args)
