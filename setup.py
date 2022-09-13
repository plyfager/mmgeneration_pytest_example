#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # 'mmgen'
]

test_requirements = [
    'pytest',
    'pytest-flake8',
    'flake8<5.0.0'
]

setup(
    author="ZOZO NZ",
    author_email='zozonz-devops@zozo.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="An example repo to show bugs when installing mmgeneration.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mmgeneration_pytest_example',
    name='mmgeneration_pytest_example',
    packages=find_packages(include=['mmgeneration_pytest_example', 'mmgeneration_pytest_example.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/zozonz/mmgeneration_pytest_example',
    version='0.1.0',
    zip_safe=False,
)
