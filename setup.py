from setuptools import setup, find_packages

setup(
    name="hibob",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "requests",  # Add other packages as a dependency
    ],
    include_package_data=True,
    description="Fork of a Python wrapper for the HiBob API",
    url="https://github.com/itsklimov/python-hibob-wrapper",
    author="Nikolay Klimov",
    author_email="itsklimov@gmail.com",
    license="MIT",
)
