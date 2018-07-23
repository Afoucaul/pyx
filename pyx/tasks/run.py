"""Pyx project execution

Usage:
    run
"""


import docopt
import subprocess
from pyx import utils as pyxutl


def main():
    pyxutl.ensure_pyx()
    _args = docopt.docopt(__doc__)

    subprocess.run(["pipenv", "run", "python", "main.py"])


if __name__ == '__main__':
    main()
