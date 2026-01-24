from setuptools import setup, find_packages

setup(
    name="pyuikit",
    version="1.1.2b1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "customtkinter",
    ],
    author="Muhammad Huzaifa Atiq",
    description="A modern UI library for Python aiming simplicity.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Huzaifa-atiq/pyuikit",
    license="MIT",
)
