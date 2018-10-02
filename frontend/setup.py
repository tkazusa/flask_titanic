# -*- encoding: UTF-8 -*-
from setuptools import setup, find_packages


setup(
    name='frontend',
    version='0.1',
    description='Frontend for titanic survival prediction app',
    author='Taketoshi Kazusa',
    author_email='takekazusa@gmail.com',
    install_requires=['flask'],
    url='https://github.com/tkazusa/flask_titanic.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)
