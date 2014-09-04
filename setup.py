#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='HPD Demo',
    version='1.0',
    description="",
    author="Peter Baumgartner",
    author_email='pete@lincolnloop.com',
    url='',
    packages=find_packages(),
    package_data={'hpd': ['static/*.*', 'templates/*.*']},
    scripts=['bin/manage.py'],
    install_requires=[
        'uwsgi==2.0.6',
        'psycopg2==2.5.3',
        'pylibmc==1.3.0',
        'fake-factory==0.4.0',
        'uwsgitop==0.8',
        'dj-database-url==0.3.0',
        'django-endless-pagination==2.0'
    ]
)
