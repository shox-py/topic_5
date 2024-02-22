from setuptools import setup

setup(
    name="topic_5",
    setup_requires=['bump2version'],
    version="{major}.{minor}.{patch}".format(**{
        "major": 1,
        "minor": 0,
        "patch": 1,
    }),
    author="Shoxrux Yuldashov",
    description="5. Основы коллекций в Python",
)
