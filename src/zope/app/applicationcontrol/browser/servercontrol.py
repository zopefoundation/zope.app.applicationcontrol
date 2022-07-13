##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
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

"""
__docformat__ = 'restructuredtext'

import zope.component

from zope.app.applicationcontrol.i18n import ZopeMessageFactory as _
from zope.app.applicationcontrol.interfaces import IServerControl


class ServerControlView(object):

    def serverControl(self):
        return zope.component.getUtility(IServerControl)

    def action(self):
        """Do the shutdown/restart!"""
        control = self.serverControl()
        time = self.request.get('time', 0)

        if 'restart' in self.request:
            control.restart(time)
            return _("The server will be restarted in ${number} seconds.",
                     mapping={"number": time})

        if 'shutdown' in self.request:
            control.shutdown(time)
            return _("The server will be shutdown in ${number} seconds.",
                     mapping={"number": time})
