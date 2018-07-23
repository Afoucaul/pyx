"""Pyx project version management

A version number is something of the form x.y.z, where z could be omitted

Usage:
    version
    version upgrade
"""

import docopt
import re
from pyx import utils as pyxutl


def print_current_version():
    settings = pyxutl.get_settings()
    pyxutl.print_info("{} - Version: {}".format(settings['name'], settings['version']))


def no_command():
    print_current_version()


def upgrade():
    print_current_version()
    version = input("New version: ")
    with open("setup.py", 'r') as setup:
        content = setup.read()

    content = re.sub(r"""(\s*'version':\s*)"[^"]*",""", r"\1'{}',".format(version), content)

    with open("setup.py", 'w') as setup:
        setup.write(content)


def main():
    pyxutl.ensure_pyx()

    args = docopt.docopt(__doc__)
    if args['upgrade']:
        upgrade()
    else:
        no_command()


if __name__ == '__main__':
    main()
