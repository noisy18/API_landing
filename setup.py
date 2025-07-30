from setuptools import setup, find_packages

setup(
    name="gears_academy_api",
    version="0.1",
    packages=find_packages(where="."),
    package_dir={"": "."},
)