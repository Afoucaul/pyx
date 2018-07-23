import setuptools

setuptools.setup(
    name="pyx-manager",
    version="1.6.3",
    entry_points={
        'console_scripts': ["pyx = pyx.__main__:main"]
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'docopt',
        'colorama'
        ],
    author='Armand Foucault',
    author_email='armand.foucault@telecom-bretagne.eu',
    description="Command-line project manager"
)
