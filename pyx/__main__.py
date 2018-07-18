"""
The Python task-oriented project manager.

Usage:
    pyx <task> [<task_args>...]
"""

import docopt
import os
import inspect
import subprocess

PYX_PATH = os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda: 0)))


def retrieve_task(name):
    local = os.path.join(os.getcwd(), ".pyx", "tasks", name + ".py")
    absolute = os.path.join(PYX_PATH, "tasks", name + ".py")

    if os.path.isfile(local):
        return local
    elif os.path.isfile(absolute):
        return absolute
    else:
        raise Exception("No such task: {}".format(name))


def main():
    args = docopt.docopt(__doc__)
    task = retrieve_task(args['<task>'])
    subprocess.run(["python3", task] + args['<task_args>'])


if __name__ == '__main__':
    main()
