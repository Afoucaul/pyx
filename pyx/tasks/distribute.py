"""Distribute your project to a PyPI repository

Usage:
    distribute
"""


import docopt
import subprocess
import pyx
import pyx.utils as pyxutl


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


def main():
    pyxutl.ensure_pyx()

    args = docopt.docopt(__doc__)

    project = pyxutl.get_project()
    pypi = project.pypi

    subprocess.run(["python3", "setup.py", "sdist", "bdist_wheel"])
    subprocess.run(twine_command(pypi))


if __name__ == '__main__':
    main()
