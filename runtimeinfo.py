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

$Id: runtimeinfo.py,v 1.4 2003/07/31 21:37:18 srichter Exp $
"""
import sys, os, time

from zope.app.interfaces.applicationcontrol import \
     IRuntimeInfo, IApplicationControl, IZopeVersion
from zope.component import getUtility, ComponentLookupError
from zope.interface import implements

class RuntimeInfo:

    implements(IRuntimeInfo)
    __used_for__ = IApplicationControl

    def __init__(self, context):
        self.context = context

    def getZopeVersion(self):
        """See zope.app.interfaces.applicationcontrol.IRuntimeInfo"""
        try:
            version_utility = getUtility(self.context, IZopeVersion)
        except ComponentLookupError:
            return ""
        return version_utility.getZopeVersion()

    def getPythonVersion(self):
        """See zope.app.interfaces.applicationcontrol.IRuntimeInfo"""
        return sys.version

    def getPythonPath(self):
        """See zope.app.interfaces.applicationcontrol.IRuntimeInfo"""
        return tuple(map(str, sys.path))

    def getSystemPlatform(self):
        """See zope.app.interfaces.applicationcontrol.IRuntimeInfo"""
        if hasattr(os, "uname"):
            return os.uname()
        else:
            return (sys.platform,)

    def getCommandLine(self):
        """See zope.app.interfaces.applicationcontrol.IRuntimeInfo"""
        return sys.argv

    def getProcessId(self):
        """See zope.app.interfaces.applicationcontrol.IRuntimeInfo"""
        return os.getpid()

    def getUptime(self):
        """See zope.app.interfaces.applicationcontrol.IRuntimeInfo"""
        return time.time() - self.context.getStartTime()

