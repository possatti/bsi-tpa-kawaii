# -*- coding: UTF-8 -*-

from distutils.core import setup

setup(
    name='Kawaii',
    version='0.1.0dev',
    author='Lucas Possatti',
    packages=['kawaii',],
    scripts=['bin/kwii',],
    url='https://github.com/possatti/kawaii',
    license="The MIT License (MIT)",
    description='Implementação do trabalho de ordenação para a disciplina de TPA.',
    long_description=open('README').read(),
)
