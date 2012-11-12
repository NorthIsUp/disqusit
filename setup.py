#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages
from sys import argv

__version__ = '0.1'


dependency_links = [
    'http://svn.edgewall.org/repos/babel/trunk'
]

install_requires = [
    'babel',
    'BabelDjango',
    'django-bootstrap-toolkit',
    'django-debug-toolbar',
    'django-social-auth',
    'gevent',
    'gunicorn',
    'path.py',
    'requests',
    'simplejson',
    ]

tests_require = [
    'unittest2',
    ]

setup_requires = []

optional_requires = {
    'nose': ('nose',),
    'cover': ('nosexcover', 'coverage',),
}

for k, v in optional_requires.iteritems():
    if True in map(lambda x: k in x, argv):
        setup_requires.extend(v)

setup(
    author='adam hitchcock',
    author_email='adam@northisup.com',
    dependency_links=dependency_links,
    description='disqus all the things!',
    include_package_data=True,
    install_requires=install_requires,
    name='disqusit',
    packages=find_packages(exclude=["tests"]),
    setup_requires=setup_requires,
    test_suite='nose.collector',
    tests_require=tests_require,
    url='http://github.com/disqus/disqusit',
    version=__version__,
    zip_safe=False,
)
