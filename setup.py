'''
MIT License

Copyright (c) 2018 Kobus Coetzer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''
from setuptools import setup, find_packages
import sshe

with open('requirements.txt') as fh:
    requires = [requirement.strip() for requirement in fh]

exclude_packages = [
    'test',
]

setup(
    name='sshe',
    version=sshe.__version__,
    description='Prints a list of available EC2 Linux instances in the specified region to connect to.',
    long_description=open('README.rst').read(),
    author=sshe.__author__,
    author_email='kobuskc@gmail.com',
    packages=find_packages(exclude=exclude_packages),
    package_dir={'sshe': 'sshe'},
    include_package_data=True,
    zip_safe=False,
    scripts=['bin/sshe'],
    install_requires=requires,
    license=open("LICENSE.txt").read(),
    classifiers=(
        'Development Status :: 0.1 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities',
    )
)
