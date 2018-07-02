#! /usr/bin/env python3

"""
The Python task-oriented project manager.

Usage:
    pyx <task>
"""

import docopt


def main(args):
    print(args['<task>'])


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    main(args)
