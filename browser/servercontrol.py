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
""" Server Control View

$Id: servercontrol.py,v 1.1 2004/03/01 13:43:25 philikon Exp $
"""
from zope.app.applicationcontrol.interfaces import IServerControl
from zope.component import getUtility

from zope.app.i18n import ZopeMessageIDFactory as _

class ServerControlView:

    def serverControl(self):
        # XXX Refactor alarm! This is *required*. We really
        # rely on it being there. If it was a utility,
        # we wouldn't care, if the ServerControl is gone,
        # but actually we do. Maybe this should be a service ...
        return getUtility(self.context, IServerControl)

    def action(self):
        """Do the shutdown/restart!"""
        if 'restart' in self.request:
            return (self.serverControl().restart()
                    or _(u"You restarted the server."))
        elif 'shutdown' in self.request:
            return (self.serverControl().shutdown()
                    or _("You shut down the server."))
