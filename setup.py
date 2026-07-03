from setuptools import setup, find_packages

setup(
    name="ghost",
    version="1.0",
    packages=find_packages(),

    py_modules=["app"],

    entry_points={
        "console_scripts": [
            "ghost=app:main"
        ]
    }
)