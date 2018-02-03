#!/usr/bin/env python

from setuptools import setup

"""
    Este script serve para definir os pacotes que serão instalados para o projeto
    e suas respectivas dependências de forma a instalar os pacotes corretos sem
    causar conflito de dependência de versões específicas.
"""



setup(name='flask',
      version='0.12.2',
      description='Python web microframework',
      author='Jackson Souza',
      author_email='jackson@ime.usp.br',
      license = "BSD",
      url='http://flask.pocoo.org/',
      python_requires='>=3',
      install_requires=['Flask==0.12.2',],
      # para realizar testes
      extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
     },
     )
