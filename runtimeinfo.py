##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
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
""" Runtime Information

$Id$
"""
__docformat__ = 'restructuredtext'

import sys, os, time

try:
    import locale
except ImportError:
    locale = None

try:
    import platform
except ImportError:
    platform = None

from zope.app.applicationcontrol.interfaces import \
     IRuntimeInfo, IApplicationControl, IZopeVersion
from zope.component import getUtility, ComponentLookupError
from zope.interface import implements

class RuntimeInfo(object):
    implements(IRuntimeInfo)
    __used_for__ = IApplicationControl

    def __init__(self, context):
        self.context = context

    def getPreferredEncoding(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        if locale is not None:
            try:
                return locale.getpreferredencoding()
            except locale.Error:
                pass
        return sys.getdefaultencoding()

    def getFileSystemEncoding(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        enc = sys.getfilesystemencoding()
        if enc is None:
            enc = self.getPreferredEncoding()
        return enc

    def getZopeVersion(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        try:
            version_utility = getUtility(IZopeVersion)
        except ComponentLookupError:
            return ""
        return version_utility.getZopeVersion()

    def getPythonVersion(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        return unicode(sys.version, self.getPreferredEncoding())

    def getPythonPath(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        enc = self.getFileSystemEncoding()
        return tuple([unicode(path, enc) for path in sys.path])

    def getSystemPlatform(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        if platform is not None:
            info = " ".join(platform.uname())
        elif hasattr(os, "uname"):
            info = " ".join(os.uname())
        else:
            info = sys.platform
        try:
            return unicode(info, self.getPreferredEncoding())
        except ValueError:
            pass
        return unicode(info, "latin1")

    def getCommandLine(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        return " ".join(sys.argv)

    def getProcessId(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        return os.getpid()

    def getUptime(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        return time.time() - self.context.getStartTime()
