import setuptools

setuptools.setup(
    name="pyx-manager",
    version="1.4",
    entry_points={
        'console_scripts': ["pyx = pyx.__main__:main"]
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'docopt',
        'colorama',
        'twine'
        ],
    author='Armand Foucault',
    author_email='armand.foucault@telecom-bretagne.eu',
    description="Command-line project manager"
)
