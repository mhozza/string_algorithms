#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    # TODO: put package requirements here
]

setup(
    name='string_algorithms',
    version='0.2.0',
    description="Collection of various string algorithms, "
                "including KMP, Aho-Corasick, Trie, SuffixArrays",
    long_description=readme,
    author="Michal Hozza",
    author_email='mhozza@gmail.com',
    url='https://github.com/mhozza/string_algorithms',
    packages=[
        'string_algorithms',
    ],
    package_dir={'string_algorithms':
                 'string_algorithms'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=True,
    keywords='string_algorithms',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
)
