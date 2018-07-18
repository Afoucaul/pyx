import setuptools

setuptools.setup(
    name="pyx-manager",
    version="1.2",
    entry_points={
        'console_scripts': ["pyx = pyx.__main__:main"]
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'docopt',
        'colorama'
        ]
)
