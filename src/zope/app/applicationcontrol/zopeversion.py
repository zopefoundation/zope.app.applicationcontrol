##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
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
"""Utility to retrieve the Zope version.
"""
__docformat__ = 'restructuredtext'

import os
import subprocess

from zope.applicationcontrol.interfaces import IZopeVersion
from zope.interface import implementer

@implementer(IZopeVersion)
class ZopeVersion(object):

    def __init__(self, path=None):
        if path is None:
            # This used to look at zope.app.__file__.  But zope.app is a
            # namespace package these days.
            # easy_install makes zope.app.__file__ be something random, like
            # /path/to/zope.app.renderer-x.y.z-py2.x.egg/zope/app/__init__.pyc
            # pip install makes zope.app have no __file__ at all, breaking
            # the old code.
            self.path = None
            self.result = "Meaningless"
        else:
            self.path = path
            self.result = None

    def getZopeVersion(self):
        """See zope.app.applicationcontrol.interfaces.IZopeVersion"""
        if self.result is not None:
            return self.result

        self.result = "Development/Unknown"

        # try to get official Zope release information
        versionfile = os.path.join(self.path, "version.txt")
        if os.path.isfile(versionfile):
            with open(versionfile) as f:
                self.result = f.readline().strip() or self.result

        return self.result


ZopeVersionUtility = ZopeVersion()
