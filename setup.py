# -*- coding: utf-8 -*-
"""
    lazy_email_validate
    ~~~~

    TBD

    :copyright: (c) 2017 by chairco <chairco@gmail.com>.
    :license: MIT.
"""

import uuid

from pip.req import parse_requirements  
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import validate


def requirements(path):  
    return [str(r.req) for r in parse_requirements(path, session=uuid.uuid1())]


class Tox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['-v', '-epy']
        self.test_suite = True

    def run_tests(self):
        import tox
        tox.cmdline(self.test_args)


setup(  
    name='lazy_email_validate',
    version=validate.__version__,
    author=validate.__author__,
    author_email=validate.__email__,
    url='https://github.com/chairco/lazy_email_validate',
    description='easy to validate email formate.',
    long_description=__doc__,
    packages=find_packages(),
    install_requires=requirements('requirements.txt'),
    tests_require=['tox'],
    cmdclass={'test': Tox},
    entry_points={'console_scripts': [
        'vtd = vtdiscourse.__main__:main',
    ]},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)