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
"""Define runtime information view component for Application Control

$Id$
"""
__docformat__ = 'restructuredtext'

from zope.app.applicationcontrol.interfaces import IRuntimeInfo

from zope.app.i18n import ZopeMessageIDFactory as _

class RuntimeInfoView:

    def runtimeInfo(self):
        formatted = {}  # will contain formatted runtime information

        try:
            runtime_info = IRuntimeInfo(self.context)
            formatted['ZopeVersion'] = runtime_info.getZopeVersion()
            formatted['PythonVersion'] = runtime_info.getPythonVersion()
            formatted['PythonPath'] = runtime_info.getPythonPath()
            formatted['SystemPlatform'] = runtime_info.getSystemPlatform()
            formatted['PreferredEncoding'] = runtime_info.getPreferredEncoding()
            formatted['FileSystemEncoding'] = runtime_info.getFileSystemEncoding()
            formatted['CommandLine'] = runtime_info.getCommandLine()
            formatted['ProcessId'] = runtime_info.getProcessId()

            # make a unix "uptime" uptime format
            uptime = long(runtime_info.getUptime())
            minutes, seconds = divmod(uptime, 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)

            uptime = _('${days} day(s) ${hours}:${minutes}:${seconds}')
            uptime.mapping = {'days': '%d' %days,
                              'hours': '%02d' %hours,
                              'minutes': '%02d' %minutes,
                              'seconds': '%02d' %seconds}

            formatted['Uptime'] = uptime

        except (TypeError, UnicodeError):
            # We avoid having errors in the ApplicationController,
            # because all those things need to stay accessible.
            na = _("n/a")
            formatted['ZopeVersion'] = na
            formatted['PythonVersion'] = na
            formatted['PythonPath'] = (na,)
            formatted['SystemPlatform'] = na
            formatted['PreferredEncoding'] = na
            formatted['FileSystemEncoding'] = na
            formatted['CommandLine'] = na
            formatted['ProcessId'] = na
            formatted['Uptime'] = na
            formatted['Hint'] = _("Could not retrieve runtime information.")

        return formatted

