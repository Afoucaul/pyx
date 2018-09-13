"""Run tests in a Pyx project.

Usage: 
    test
"""

import sys
import os
import subprocess
import importlib
import docopt
import pyx.utils as pyxutl


TESTERS = ["pytest", "unittest"]


def get_tester():
    tester = None
    for t in TESTERS:
        try:
            tester = importlib.import_module(t)
        except ImportError:
            pass

        if tester is not None:
            break

    return t


def cmd_pytest():
    return ["python3", "-m", "pytest"]


def cmd_unittest():
    return ["python3", "-m", "unittest", "discover", "-v", "test"]
    

def cmd_default(tester):
    return ["python3", "-m", tester]


def main(args):
    tester = get_tester()
    if tester is None:
        pyxutl.print_error("No test runner found")
        sys.exit(1)

    try:
        cmd = globals()["cmd_{}".format(tester)]()
        if pyxutl.is_pipenv():
            cmd = ["pipenv", "run"] + cmd
        subprocess.run(cmd)
    except KeyError:
        run_default(tester)


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    main(args)
