##############################################################################
#
# Copyright (c) Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################

import os

from setuptools import setup, find_packages

version = '4.0.0.dev0'

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

tests_require = [
    'webtest',

    'zope.app.authentication >= 4.0.0',
    'zope.app.basicskin >= 4.0.0',
    'zope.app.form >= 5.0.0',
    'zope.app.locales >= 4.0.0',
    'zope.app.publication',
    'zope.app.rotterdam >= 4.0.0',
    'zope.app.wsgi',

    'zope.browserresource >= 4.1.0',
    'zope.login',
    'zope.password',
    'zope.principalregistry',
    'zope.securitypolicy',
    'zope.testbrowser >= 5.2',
    'zope.testrunner',
]

setup(name='zope.app.applicationcontrol',
    version = version,
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    description='Zope application control',
    long_description=(
        read('README.rst')
        + '\n\n' +
        read('CHANGES.rst')
        ),
    license='ZPL 2.1',
    keywords="zope3 application control",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3',
    ],
    url='http://github.com/zopefoundation/zope.app.applicationcontrol',
    extras_require={
        'test': tests_require,
    },
    package_dir={'': 'src'},
    packages=find_packages('src'),
    namespace_packages=['zope', 'zope.app'],
    install_requires=[
          'setuptools',
          'ZODB',
          'zope.applicationcontrol >= 4.0.1',
          'zope.component',
          'zope.i18n',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.size',
          'zope.traversing>=3.7.0',
        ],
    include_package_data=True,
    zip_safe=False,
)
