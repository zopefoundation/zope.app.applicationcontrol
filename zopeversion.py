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
"""Utility to retrieve the Zope version.

$Id$
"""
import os
import re

import zope.app
from zope.app.applicationcontrol.interfaces import IZopeVersion
from zope.interface import implements

class ZopeVersion(object):
    implements(IZopeVersion)

    __entries = re.compile(r'(url|revision)\s*=\s*"([^"]+)"')
    __tags = re.compile(r'/(tags|branches)/([^/]+)/')

    def __init__(self, path=None):
        if path is None:
            path = os.path.dirname(os.path.abspath(zope.app.__file__))
        self.path = path
        self.result = None

    def getZopeVersion(self):
        """See zope.app.applicationcontrol.interfaces.IZopeVersion"""
        if self.result is not None:
            return self.result

        self.result = "Development/Unknown"

        # is this a SVN checkout?
        svndir = os.path.join(self.path, ".svn")
        if os.path.isdir(svndir):
            self.__setSVNVersion(svndir)
        else:
            # try to get official Zope release information
            versionfile = os.path.join(self.path, "version.txt")
            if os.path.isfile(versionfile):
                f = file(versionfile)
                self.result = f.readline().strip() or self.result
                f.close()
        return self.result

    def __setSVNVersion(self, svndir):
            entriesfile = os.path.join(svndir, "entries")

            # get the version information
            if os.path.isfile(entriesfile):
                f = file(entriesfile)
                url, revision = "", ""
                for line in f:
                    match = self.__entries.search(line)
                    if match is not None:
                        name, value = match.group(1, 2)
                        if name == "url":
                            url = value
                        elif name == "revision":
                            revision = value
                        if url and revision:
                            break
                f.close()

                if revision and url:
                    match = self.__tags.search(url)
                    tag = ""
                    if match is not None:
                        type, value = match.group(1, 2)
                        if type == "tags":
                            tag = "/Tag: %s" % value
                        elif type == "branches":
                            tag = "/Branch: %s" % value
                    self.result = "Development/Revision: %s%s" \
                                  % (revision, tag)

ZopeVersionUtility = ZopeVersion()
