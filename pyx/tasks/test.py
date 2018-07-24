"""Run tests in a Pyx project.

Usage: 
    test
"""

import os
import docopt
import subprocess


def main(args):
    subprocess.run(["python3", "-m", "unittest", "-v", "discover", "test"])


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    main(args)
