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
"""Zope version

$Id: zopeversion.py,v 1.7 2004/04/30 14:30:42 fdrake Exp $"""

import os

import zope
from zope.app.applicationcontrol.interfaces import IZopeVersion
from zope.interface import implements

class ZopeVersion:

    implements(IZopeVersion)

    def getZopeVersion(self):
        """See zope.app.applicationcontrol.interfaces.IZopeVersion"""

        version_id = "Development/Unknown"
        version_tag = ""
        is_cvs = 0

        zopedir = os.path.dirname(zope.__file__)

        # is this a CVS checkout?
        cvsdir = os.path.join(zopedir, "CVS" )
        if os.path.isdir(cvsdir):
            is_cvs = 1
            tagfile = os.path.join(cvsdir, "Tag")

            # get the tag information
            if os.path.isfile(tagfile):
                f = open(tagfile)
                tag = f.readline().rstrip()
                f.close()
                if tag.startswith("T"):
                    version_tag = " (%s)" % tag[1]

        # try to get official Zope release information
        versionfile = os.path.join(zopedir, "version.txt")
        if os.path.isfile(versionfile) and not is_cvs:
            f = open(versionfile)
            version_id = f.readline().strip() or version_id
            f.close()

        version = "%s%s" % (version_id, version_tag)
        return version

ZopeVersionUtility = ZopeVersion()
