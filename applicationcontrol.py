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

import time

from zope.security.checker import ProxyFactory, NamesChecker
from zope.interface import implements

from zope.app.location import Location
from zope.app.folder import rootFolder
from zope.app.applicationcontrol.interfaces import IApplicationControl

class ApplicationControl(Location):

    implements(IApplicationControl)

    def __init__(self):
        self.start_time = time.time()

    def getStartTime(self):
        return self.start_time

applicationController = ApplicationControl()
applicationControllerRoot = ProxyFactory(rootFolder(),
                                         NamesChecker("__class__"))
applicationController.__parent__ = applicationControllerRoot
applicationController.__name__ = '++etc++process'
