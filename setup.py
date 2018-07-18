import setuptools

setuptools.setup(
    entry_points={
        'console_scripts': ["pyx = pyx.__main__:main"]
    },
    name="pyx-manager",
    packages=setuptools.find_packages(),
    version="1.2"
)
