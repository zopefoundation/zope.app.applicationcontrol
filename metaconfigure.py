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
""" Register ServerControl configuration directives.

$Id: metaconfigure.py,v 1.5 2003/08/17 06:05:20 philikon Exp $
"""

from zope.component import getUtility
from zope.app.interfaces.applicationcontrol import IServerControl

def registerShutdownHook(_context, call, name, priority):
    """Register a shutdown hook with the current server control utility"""
    _context.action(
        discriminator = ('server-control:registerShutdownHook', name),
        callable = doRegisterShutdownHook,
        args = (_context, call, priority, name)
        )

def doRegisterShutdownHook(_context, call, priority, name):
    server_control = getUtility(_context, IServerControl)
    server_control.registerShutdownHook(call, priority, name)
