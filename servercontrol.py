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
__doc__ = """ Server Control Implementation

$Id: servercontrol.py,v 1.2 2002/12/25 14:12:25 jim Exp $"""

from zope.app.interfaces.applicationcontrol.servercontrol import \
  IServerControl, ServerControlError, DoublePriorityError, NotCallableError
import logging

import sys


class ServerControl:

    __implements__ = IServerControl

    def __init__(self):
        self._shutdown_reg = {}    # This is the actual shutdown registry.
                                   # It will hold the hooks accessible by their
                                   # priority. The priority actually needs to be
                                   # a floating point value, to allow most fine
                                   # grained control on the priority.


    def shutdown(self):
        text = ""
        order = self._shutdown_reg.keys()
        order.sort()

        for hook_ in order:
            hook = self._shutdown_reg[hook_]
            hook[0]()

    def restart(self):
        'XXX'

    def registerShutdownHook(self, call, priority, name):
        priority = float(priority)
        if priority in self._shutdown_reg:
            raise DoublePriorityError, (call, priority, name)

        if not callable(call):
            raise NotCallableError, (call, priority, name)

        self._shutdown_reg.update({priority: (call, name)})


    #
    ############################################################



## simple log notification for shutdown
def shutdownLogger():
    """simple shutdown logger"""
    logging.warn("ServerControl: Server is going to be shut down.")
