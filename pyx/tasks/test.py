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


def run_with_pytest():
    subprocess.run(["python3", "-m", "pytest"])


def run_with_unittest():
    subprocess.run(["python3", "-m", "unittest", "discover", "-v", "test"])
    

def run_default(tester):
    subprocess.run(["python3", "-m", tester])


def main(args):
    tester = get_tester()
    if tester is None:
        pyxutl.print_error("No test runner found")
        sys.exit(1)

    try:
        globals()["run_with_{}".format(tester)]()
    except KeyError:
        run_default(tester)


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    main(args)
