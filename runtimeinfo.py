##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Runtime Information

$Id: runtimeinfo.py,v 1.8 2004/03/25 14:37:08 hdima Exp $
"""
import sys, os, time

try:
    import locale
except ImportError:
    locale = None

from zope.app.applicationcontrol.interfaces import \
     IRuntimeInfo, IApplicationControl, IZopeVersion
from zope.component import getUtility, ComponentLookupError
from zope.interface import implements

class RuntimeInfo:

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
            version_utility = getUtility(self.context, IZopeVersion)
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
        # FIXME: platform.platform()?
        if hasattr(os, "uname"):
            info = os.uname()
        else:
            info = (sys.platform,)
        return unicode(" ".join(info), self.getPreferredEncoding())

    def getCommandLine(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        return " ".join(sys.argv)

    def getProcessId(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        return os.getpid()

    def getUptime(self):
        """See zope.app.applicationcontrol.interfaces.IRuntimeInfo"""
        return time.time() - self.context.getStartTime()

