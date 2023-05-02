from setuptools import setup

from predstr import __version__

setup(
    name="predstr",
    version=__version__,
    url="https://github.com/HKozubek/PredictionStrength",
    author="Hubert Kozubek",
    author_email="hkozubek00@gmail.com",
    py_modules=["predstr"],
    install_requires=[
        "numpy",
    ],
)
