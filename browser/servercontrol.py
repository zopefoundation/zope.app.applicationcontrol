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

from zope.app.i18n import ZopeMessageFactory as _

class ServerControlView(object):

    def serverControl(self):
        return zapi.getUtility(IServerControl)

    def action(self):
        """Do the shutdown/restart!"""
        # XXX I18N the responses
        control = self.serverControl()

        if 'time' in self.request:
            time = self.request.get('time', 0)

        if 'restart' in self.request:
            control.restart(time)
            return u"The server will be restarted in %s seconds." % time
        elif 'shutdown' in self.request:
            control.shutdown(time)
            return u"The server will be shutdown in %s seconds." % time

