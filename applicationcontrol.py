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
""" Application Control

$Id: applicationcontrol.py,v 1.7 2004/02/24 16:51:50 philikon Exp $"""

import time

from zope.security.checker import ProxyFactory, NamesChecker
from zope.interface import implements

from zope.app import zapi
from zope.app.location import Location
from zope.app.folder import rootFolder
from zope.app.interfaces.applicationcontrol import IApplicationControl

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
