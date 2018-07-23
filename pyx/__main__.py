"""The Python task-oriented project manager.

Usage:
    pyx 
    pyx <task> [<task_args>...]
"""

import docopt
import os
import inspect
import subprocess
from pyx import utils as pyxutl

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


def execute_task(task_name):
    task = retrieve_task(task_name)
    subprocess.run(["python3", task] + task_name)


def print_command_list():
    tasks = pyxutl.get_tasks()
    print("Tasks:")
    pyxutl.print_list(tasks)


def main():
    args = docopt.docopt(__doc__)
    task_name = args['<task>']
    if task_name is not None:
        execute_task(args['<task_args>'])
    else:
        print(__doc__)
        print_command_list()


if __name__ == '__main__':
    main()
