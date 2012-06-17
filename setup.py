#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

install_requires = [
    'Flask',
    'gevent',
    'gunicorn',
    'logutils',
    'ordereddict',
    'path.py',
    'Paver',
    'progressbar',
    'simplejson',
    'requests'
    'wtforms'
    'flask-sqlalchemy'
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
