##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
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
"""Setup for zope.app.applicationcontrol package

$Id$
"""

import os

try:
    from setuptools import setup, Extension
except ImportError, e:
    from distutils.core import setup, Extension

setup(name='zope.app.applicationcontrol',
      version='3.4-dev',
      url='http://svn.zope.org/zope.app.applicationcontrol',
      license='ZPL 2.1',
      description='Zope applicationcontrol',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      long_description="The application control instance is usually"
                       "generated upon startup.  This package provides"
                       "runtime information adapter for application"
                       "control and Zope version.  Also provide a utility"
                       "with methods for shutting down and"
                       "restarting the server.",

      extras_require=dict(test=['zope.app.testing']),

      packages=['zope', 'zope.app',
                'zope.app.applicationcontrol',
                'zope.app.applicationcontrol.browser',
                'zope.app.applicationcontrol.browser.ftests',
                'zope.app.applicationcontrol.browser.tests',
                'zope.app.applicationcontrol.tests'],
      package_dir = {'': 'src'},

      namespace_packages=['zope', 'zope.app'],
      install_requires=['zope.interface',
                        'zope.i18n',
                        'zope.size'],
      include_package_data = True,

      zip_safe = False,
      )
