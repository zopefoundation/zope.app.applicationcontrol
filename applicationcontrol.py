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
__doc__ = """ Application Control

$Id: applicationcontrol.py,v 1.2 2002/12/25 14:12:25 jim Exp $"""

from zope.app.interfaces.applicationcontrol.applicationcontrol import IApplicationControl
from zope.app.content.folder import RootFolder
from zope.security.checker import ProxyFactory, NamesChecker

import time

class ApplicationControl:
    """ """

    __implements__ = IApplicationControl

    def __init__(self):
        self.start_time = time.time()


    def getStartTime(self):
        return self.start_time

    #
    ############################################################

applicationController = ApplicationControl()
applicationControllerRoot = ProxyFactory(RootFolder(),
                                         NamesChecker("__class__"))
