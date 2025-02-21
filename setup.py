#!/usr/bin/env python
""" Password strength and validation """

from setuptools import setup, find_packages

setup(
    name='py-password_strength',
    version='0.0.5',
    author='Mark Vartanyan',
    author_email='kolypto@gmail.com',

    url='https://github.com/jam-py-v5/py-password-strength',
    license='BSD',
    description=__doc__,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['password', 'strength', 'policy', 'security'],

    packages=find_packages(),
    scripts=[],
    entry_points={},

    install_requires=[
        'six',
    ],
    extras_require={
    },
    include_package_data=True,
    test_suite='nose.collector',

    platforms='any',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
