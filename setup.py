from setuptools import setup, find_packages

packages = find_packages(where='src')
print(packages)

setup(
    name="dtxmp",
    version="0.1",
    author="Ryan Grout",
    description="Library for accessing and interpreting darktable XMP files",
    python_requires=">=3.6",
    packages=packages,
    package_dir={'':'src'},
    requires=['lxml']
)