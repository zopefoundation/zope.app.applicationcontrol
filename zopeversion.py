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
"""Utility to retrieve the Zope version.

$Id: zopeversion.py,v 1.10 2004/05/03 14:17:04 fdrake Exp $
"""

import os

import zope
from zope.app.applicationcontrol.interfaces import IZopeVersion
from zope.interface import implements

class ZopeVersion:

    implements(IZopeVersion)

    def __init__(self, path=None):
        if path is None:
            path = os.path.dirname(os.path.abspath(zope.__file__))
        self.path = path
        self.result = None

    def getZopeVersion(self):
        """See zope.app.applicationcontrol.interfaces.IZopeVersion"""
        if self.result is not None:
            return self.result

        version_id = "Development/Unknown"
        version_tag = ""
        is_cvs = False

        # is this a CVS checkout?
        # XXX need to change this when we move to Subversion
        cvsdir = os.path.join(self.path, "CVS" )
        if os.path.isdir(cvsdir):
            is_cvs = True
            tagfile = os.path.join(cvsdir, "Tag")

            # get the tag information
            if os.path.isfile(tagfile):
                f = open(tagfile)
                tag = f.readline().rstrip()
                f.close()
                if tag.startswith("T"):
                    version_tag = " (%s)" % tag[1:]

        # try to get official Zope release information
        versionfile = os.path.join(self.path, "version.txt")
        if os.path.isfile(versionfile) and not is_cvs:
            f = open(versionfile)
            version_id = f.readline().strip() or version_id
            f.close()

        self.result = "%s%s" % (version_id, version_tag)
        return self.result

ZopeVersionUtility = ZopeVersion()
