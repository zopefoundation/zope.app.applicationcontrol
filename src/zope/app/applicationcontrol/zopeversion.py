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
"""Utility to retrieve the Zope version.

$Id$
"""
__docformat__ = 'restructuredtext'

import os
import re
import subprocess

from zope.applicationcontrol.interfaces import IZopeVersion
from zope.interface import implements


class ZopeVersion(object):

    implements(IZopeVersion)

    __tags = re.compile(r'/(tags|branches)/([^/]+)/')

    def __init__(self, path=None):
        if path is None:
            # This used to look at zope.app.__file__.  But zope.app is a
            # namespace package these days.
            # easy_install makes zope.app.__file__ be something random, like
            # /path/to/zope.app.renderer-x.y.z-py2.x.egg/zope/app/__init__.pyc
            # pip install makes zope.app have no __file__ at all, breaking
            # the old code.
            self.path = None
            self.result = "Meaningless"
        else:
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
                try:
                    self.result = f.readline().strip() or self.result
                finally:
                    f.close()
        return self.result

    def _getSVNInfoOutput(self):
        try:
            env = os.environ.copy()
            env['LANG'] = env['LC_ALL'] = env['LC_MESSAGES'] = 'C'
            proc = subprocess.Popen('svn info "%s"' % self.path,
                shell=True, stdout=subprocess.PIPE, env=env)
        except OSError:
            pass
        else:
            if proc.wait() == 0:
                return proc.stdout
        return None

    def __setSVNVersion(self, svndir):
        output = self._getSVNInfoOutput()
        if not output:
            return

        info = {}
        for line in output:
            parts = line.rstrip().split(": ", 1)
            if len(parts) == 2:
                key, value = parts
                info[key] = value

        revision = info.get("Revision", "")
        url = info.get("URL", "")

        if revision and url:
            match = self.__tags.search(url)
            if match is None:
                tag = ""
            else:
                type, value = match.groups()
                if type == "tags":
                    tag = "/Tag: %s" % value
                elif type == "branches":
                    tag = "/Branch: %s" % value
            self.result = ("Development/Revision: %s%s"
                          % (revision, tag))

ZopeVersionUtility = ZopeVersion()
