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
""" Server Control View

$Id$
"""
__docformat__ = 'restructuredtext'

from ZODB.FileStorage.FileStorage import FileStorageError
from zope.app.i18n import ZopeMessageIDFactory as _

class ZODBControlView(object):

    def getName(self):
        """Get the database name."""
        return self.request.publication.db.getName()

    def getSize(self):
        """Get the database size in a human readable format."""
        size = self.request.publication.db.getSize()
        if size > 1024**2:
            size_str = _("${size} MB")
            size_str.mapping = {'size': "%.1f" %(float(size)/1024**2)}
        elif size > 1024:
            size_str = _("${size} kB")
            size_str.mapping = {'size': "%.1f" %(float(size)/1024)}
        else:
            size_str = _("${size} Bytes")
            size_str.mapping = {'size': "%i" %size}

        return size_str
        

    def pack(self):
        """Do the packing!"""
        days = int(self.request.form.get('days', 0))
        status = ''
        if 'PACK' in self.request:
            try:
                self.request.publication.db.pack(days=days)
                status = _('ZODB successfully packed.')
            except FileStorageError, err:
                status = _(err)
                
        return status
