"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-extreme-tdd',

    version='0.1.0',

    description='Testing toolkit to advocate real and fast TDD (testing first!) in Django applications, eXtremeProgramming like!',
    long_description=long_description,

    url='https://github.com/flaviamissi/django-extreme-tdd',

    author='Flavia Missi',
    author_email='flaviamissi@gmail.com',

    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing Tools',

        'License :: OSI Approved :: BSD License',

        # 'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
    ],

    keywords='testing tdd development django',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['docs', 'tests*']),

    # https://packaging.python.org/en/latest/requirements.html
    # TODO: get from file
    install_requires=['django>=1.4'],

    # $ pip install -e .[dev,test]
    # TODO: get from file
    extras_require={
        'dev': ['mkdocs'],
        'test': ['nose'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
