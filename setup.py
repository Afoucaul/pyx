import setuptools

with open("PYPI_README.md", 'r') as f:
    readme = f.read()

setuptools.setup(
    name="pyx-manager",
    version="1.6.8",
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
    description="Command-line project manager",
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://github.com/Afoucaul/pyx"
)
