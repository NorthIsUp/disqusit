#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

install_requires = [
    'anyjson==0.3.1',
    'argparse==1.2.1',
    'disqus-flask==0.1.18',
    'Flask==0.8',
    'gevent==1.0b2',
    'gunicorn==0.13.4',
    'hiredis==0.1.0',
    'logutils==0.3.2',
    'mrsdash==0.1.17',
    'ordereddict==1.1',
    'paste==1.7.5.1',
    'path.py==2.2.2',
    'Paver==1.0.5',
    'progressbar==2.3',
    'raven==1.9.3',
    'scales==1.0.2',
    'simplejson==2.4.0',
    'thoonk==1.0.1.0',
    'ujson==1.18',
    ]

package_data = {
    'realertime': [
        r'config/*.json'
        ],
}

tests_require = [
    'Flask-Testing',
    'mock==0.8',
    'pyflakes',
    'unittest2',
    ]

setup_requires = [
    'nose',
    'nosexcover',
]

setup(
    author='Adam Hitchcock',
    author_email='adam@disqus.com',
    description='Real time server based around gevent',
    include_package_data=True,
    install_requires=install_requires,
    name='disqusit',
    packages=find_packages(exclude=["tests"]),
    package_data=package_data,
    setup_requires=setup_requires,
    test_suite='nose.collector',
    tests_require=tests_require,
    version=0.1,
    zip_safe=False,
)
