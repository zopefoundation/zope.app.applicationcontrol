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
"""Application Control

$Id$"""

from zope.app.applicationcontrol.interfaces import IApplicationControl
from zope.app.location import Location
from zope.security.checker import ProxyFactory, NamesChecker
import time
import zope.interface
import zope.app.traversing.interfaces

class ApplicationControllerRoot(Location):
    zope.interface.implements(zope.app.traversing.interfaces.IContainmentRoot)

class ApplicationControl(Location):

    zope.interface.implements(IApplicationControl)

    def __init__(self):
        self.start_time = time.time()

    def getStartTime(self):
        return self.start_time

applicationController = ApplicationControl()
applicationControllerRoot = ProxyFactory(ApplicationControllerRoot(),
                                         NamesChecker("__class__"))
applicationController.__parent__ = applicationControllerRoot
applicationController.__name__ = '++etc++process'
