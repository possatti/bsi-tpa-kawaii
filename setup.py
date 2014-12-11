# -*- coding: UTF-8 -*-

from distutils.core import setup

setup(
    name='Kawaii',
    version='0.1.0dev',
    author='Lucas Possatti',
    packages=['kawaii',],
    scripts=['bin/helloer',],
    url='https://github.com/possatti/kawaii',
    license=open('LICENSE').read(),
    description='Implementação do trabalho de ordenação para a disciplina de TPA.',
    long_description=open('README').read(),
)