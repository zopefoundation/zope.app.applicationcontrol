##############################################################################
#
# Copyright (c) 2003 Zope Corporation and Contributors.
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
"""ZODB Control

$Id: zodbcontrol.py,v 1.1 2003/07/31 21:37:18 srichter Exp $
"""
import os
from zope.interface import implements
from zope.app.interfaces.applicationcontrol import \
     IApplicationControl, IZODBControl

class ZODBControl:

    implements(IZODBControl)
    __used_for__ = IApplicationControl

    def __init__(self, context):
        self.context = context

    def getDatabaseSize(self, db):
        """See zope.app.interfaces.applicationControl.IZODBControl"""
        return os.path.getsize(db._storage._file_name)

    def pack(self, db, days):
        """See zope.app.interfaces.applicationControl.IZODBControl"""
        db.pack(days=days)
