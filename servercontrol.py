##############################################################################
#
# Copyright (c) 2001,2002,2003 Zope Corporation and Contributors.
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
"""Server Control Implementation

$Id: servercontrol.py,v 1.3 2003/01/02 15:48:46 bwarsaw Exp $
"""

import sys
import logging

from zope.app.interfaces.applicationcontrol.servercontrol import \
     IServerControl, ServerControlError, DoublePriorityError, NotCallableError


class ServerControl:

    __implements__ = IServerControl

    def __init__(self):
        # This is the actual shutdown registry.  It will hold the hooks
        # accessible by their priority. The priority actually needs to be a
        # floating point value, to allow most fine grained control on the
        # priority.
        self._shutdown_reg = {}

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
