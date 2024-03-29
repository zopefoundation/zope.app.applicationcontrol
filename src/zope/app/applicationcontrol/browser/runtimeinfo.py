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
"""Define runtime information view component for Application Control
"""
__docformat__ = 'restructuredtext'

from zope.app.applicationcontrol.i18n import ZopeMessageFactory as _
from zope.app.applicationcontrol.interfaces import IRuntimeInfo


class RuntimeInfoView:

    _fields = (
        "ZopeVersion",
        "PythonVersion",
        "PythonPath",
        "SystemPlatform",
        "PreferredEncoding",
        "FileSystemEncoding",
        "CommandLine",
        "ProcessId",
        "DeveloperMode",
    )
    _unavailable = _("Unavailable")

    def runtimeInfo(self):
        try:
            ri = IRuntimeInfo(self.context)
        except TypeError:
            formatted = dict.fromkeys(self._fields, self._unavailable)
            formatted["Uptime"] = self._unavailable
        else:
            formatted = self._getInfo(ri)
        return formatted

    def _getInfo(self, ri):
        formatted = {}
        for name in self._fields:
            value = self._unavailable
            try:
                value = getattr(ri, "get" + name)()
            except ValueError:  # pragma: no cover
                pass
            formatted[name] = value
        formatted["Uptime"] = self._getUptime(ri)
        return formatted

    def _getUptime(self, ri):
        # make a unix "uptime" uptime format
        uptime = int(ri.getUptime())
        minutes, seconds = divmod(uptime, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        return _('${days} day(s) ${hours}:${minutes}:${seconds}',
                 mapping={'days': '%d' % days,
                          'hours': '%02d' % hours,
                          'minutes': '%02d' % minutes,
                          'seconds': '%02d' % seconds})
