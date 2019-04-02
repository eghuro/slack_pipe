#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'atenvironment', 'slackclient']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Alexandr Mansurov",
    author_email='alex@eghuro.cz',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring'
    ],
    description="Pipe messages from shell to Slack.",
    entry_points={
        'console_scripts': [
            'slack_pipe=slack_pipe.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='slack_pipe',
    name='slack_pipe',
    packages=find_packages(include=['slack_pipe']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/eghuro/slack_pipe',
    version='1.0.0',
    zip_safe=False,
)
