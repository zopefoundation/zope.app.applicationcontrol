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

$Id: zodbcontrol.py,v 1.5 2004/03/01 13:43:24 philikon Exp $
"""
from zope.interface import implements
from zope.app.applicationcontrol.interfaces import \
     IApplicationControl, IZODBControl

class ZODBControl:

    implements(IZODBControl)
    __used_for__ = IApplicationControl

    def __init__(self, context):
        self.context = context

    def getDatabaseSize(self, db):
        """See zope.app.applicationcontrol.interfaces.IZODBControl"""
        # XXX ZODB 4 doesn't support getting the database size
        # the original implementation (commnted out) depended on internal
        # file-storage implementation details.
        
        # return os.path.getsize(db._storage._file_name)
        return 0

    def pack(self, db, days):
        """See zope.app.applicationcontrol.interfaces.IZODBControl"""
        db.pack(days=days)
