##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Server Control View

$Id$
"""
__docformat__ = 'restructuredtext'

from zope.app import zapi
from zope.app.applicationcontrol.interfaces import IServerControl

from zope.app.i18n import ZopeMessageIDFactory as _

class ServerControlView(object):

    def serverControl(self):
        return zapi.getUtility(IServerControl)

    def action(self, time=0):
        """Do the shutdown/restart!"""
        if 'restart' in self.request:
            return (self.serverControl().restart(time)
                    or _(u"You restarted the server."))
        elif 'shutdown' in self.request:
            return (self.serverControl().shutdown(time)
                    or _("You shut down the server."))
