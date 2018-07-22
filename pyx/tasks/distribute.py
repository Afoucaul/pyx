"""Distribute your project to a PyPI repository

Usage:
    distribute [<config>]
"""


import docopt
import subprocess
import pyx
import pyx.utils as pyxutl
import pyx.errors as pyxerr


def twine_command(args):
    cmd = ["twine", "upload"]

    if 'repository' in args:
        cmd.extend(["--repository-url", args['repository']])

    if 'username' in args:
        cmd.extend(["-u", args['username']])

    if 'password' in args:
        cmd.extend(["-p", args["password"]])

    cmd.extend(["--skip-existing", "dist/*"])

    print(cmd)
    return cmd


def prepare_args(args):
    if args['<config>'] is None:
        args['<config>'] = "default"


def main():
    pyxutl.ensure_pyx()

    args = docopt.docopt(__doc__)
    prepare_args(args)

    config = pyx.Config.get(args['<config>'])
    try:
        pypi = config.pypi
    except AttributeError:
        raise pyxerr.ConfigError(config, "pypi")

    subprocess.run(["python3", "setup.py", "sdist", "bdist_wheel"])
    subprocess.run(twine_command(pypi))


if __name__ == '__main__':
    main()
