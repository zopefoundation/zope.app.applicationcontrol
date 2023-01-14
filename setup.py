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

from setuptools import find_packages
from setuptools import setup


version = '5.0.dev0'


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


tests_require = [
    'webtest',

    'zope.app.appsetup>=4.0.0',
    'zope.app.authentication>=4.0.0',
    'zope.app.basicskin>=4.0.0',
    'zope.app.component>=4.0.0',
    'zope.app.container>=4.0.0',
    'zope.app.locales>=4.0.0',
    'zope.app.pagetemplate>=4.0.0',
    'zope.app.publication>=4.2.1',
    'zope.app.wsgi>=4.1.0',
    'zope.applicationcontrol>=4.0.1',
    'zope.authentication>=4.2.1',

    'zope.annotation>=4.4.1',
    'zope.browser>=2.1.0',
    'zope.browsermenu>=4.1.1',
    'zope.browserpage>=4.1.0',
    'zope.browserresource>=4.1.0',
    'zope.container>=4.1.0',
    'zope.formlib>=4.3.0',
    'zope.i18nmessageid>=4.1.0',
    'zope.interface>=4.4.0',
    'zope.login>=2.0.0',
    'zope.pagetemplate>=4.2.1',
    'zope.password>=4.2.0',
    'zope.pluggableauth>=2.2.0',
    'zope.principalregistry>=4.0.0',
    'zope.publisher>=4.3.1',
    'zope.schema>=4.4.2',
    'zope.securitypolicy>=4.1.0',
    'zope.session>=4.1.0',
    'zope.site>=4.0.0',
    'zope.testbrowser>=5.2',
    'zope.testing',
    'zope.testrunner',
]

setup(name='zope.app.applicationcontrol',
      version=version,
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
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope :: 3',
      ],
      url='https://github.com/zopefoundation/zope.app.applicationcontrol',
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
