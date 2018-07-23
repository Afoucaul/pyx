"""Distribute your project to a PyPI repository

Usage:
    release
"""


import docopt
import subprocess
import sys
import shutil
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


def git_release():
    version = pyxutl.get_settings()['version']
    subprocess.run(["git", "tag", "-a", version])


def main():
    pyxutl.ensure_pyx()

    args = docopt.docopt(__doc__)

    project = pyxutl.get_project()
    pypi = project.pypi

    version = pyxutl.get_settings()['version']
    message = "The project will be released as version {}. Are you sure?"
    if not pyxutl.prompt(message.format(version)):
        sys.exit(0)

    shutil.rmtree("build", ignore_errors=True)
    if pyxutl.is_git():
        git_release()
    subprocess.run(["python3", "setup.py", "sdist", "bdist_wheel"])
    subprocess.run(twine_command(pypi))


if __name__ == '__main__':
    main()
