"""Pyx project execution

Usage:
    run [<config>]
"""


import docopt
import pyx
import sys
import os


def main(args):
    app = pyx.Application.get()
    config = pyx.Config.get(args['<config>'])
    app(config).run()


def prepare_args(args):
    if args['<config>'] is None:
        args['<config>'] = "default"


if __name__ == '__main__':
    sys.path.append(os.getcwd())
    args = docopt.docopt(__doc__)
    prepare_args(args)

    main(args)
