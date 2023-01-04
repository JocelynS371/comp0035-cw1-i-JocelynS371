from setuptools import setup

setup(
    name="comp0035-cw-testing",
    version="1.0.0",
    packages=["src"],
    package_dir={
    "src": "./coursework2/src",},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],)
