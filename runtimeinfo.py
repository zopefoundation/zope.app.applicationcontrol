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
__doc__ = """ Runtime Information

$Id: runtimeinfo.py,v 1.2 2002/12/25 14:12:25 jim Exp $"""

from zope.app.interfaces.applicationcontrol.runtimeinfo import IRuntimeInfo
from zope.app.interfaces.applicationcontrol.applicationcontrol import IApplicationControl
from zope.component import getUtility, ComponentLookupError
from zope.app.interfaces.applicationcontrol.zopeversion import IZopeVersion
import sys, os, time

class RuntimeInfo:

    __implements__ =  IRuntimeInfo
    __used_for__ = IApplicationControl

    def __init__(self, context):
        self.context = context

    def getZopeVersion(self):
        try:
            version_utility = getUtility(self.context, IZopeVersion)
        except ComponentLookupError:
            return ""
        return version_utility.getZopeVersion()

    def getPythonVersion(self):
        return sys.version

    def getPythonPath(self):
        return tuple(map(str, sys.path))

    def getSystemPlatform(self):
        if hasattr(os, "uname"):
            return os.uname()
        else:
            return (sys.platform,)

    def getCommandLine(self):
        return sys.argv

    def getProcessId(self):
        return os.getpid()

    def getUptime(self):
        return time.time() - self.context.getStartTime()

    #
    ############################################################
