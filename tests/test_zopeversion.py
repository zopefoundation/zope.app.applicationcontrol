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
"""Zope Version Tests

$Id$
"""
import os
import shutil
import tempfile
import unittest

from zope.interface.verify import verifyObject
from zope.app.applicationcontrol.interfaces import IZopeVersion
from zope.app.applicationcontrol.zopeversion import ZopeVersion

class Test(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="test-zopeversion-")

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def prepare(self, version, tag):
        if version:
            f = open(os.path.join(self.tmpdir, "version.txt"), "w")
            f.write(version)
            if not version.endswith("\n"):
                f.write("\n")
            f.close()
        if tag:
            os.mkdir(os.path.join(self.tmpdir, "CVS"))
            f = open(os.path.join(self.tmpdir, "CVS", "Tag"), "w")
            f.write(tag)
            if not tag.endswith("\n"):
                f.write("\n")
            f.close()

    def _Test__new(self):
        return ZopeVersion(self.tmpdir)

    def test_IVerify(self):
        verifyObject(IZopeVersion, self._Test__new())

    # CVS/Tag lines can start with different characters, each of which
    # has some meaning:
    #   D - checked out with a date; format is YYYY.MM.DD.HH.MM.SS
    #       where HH.MM.SS indicates timezone (04.00.00 is GMT - 4 hours)
    #   N - checked out with a non-branch tag; format is Ntagname
    #   T - checked out with a branch tag; format is Ttagname

    def test_ZopeVersion(self):
        self.prepare(None, None)
        zope_version = self._Test__new()
        self.assertEqual(zope_version.getZopeVersion(), "Development/Unknown")

    def test_ZopeVersion_cvsdate(self):
        self.prepare(None, "D2004.04.30.04.00.00")
        zope_version = self._Test__new()
        self.assertEqual(zope_version.getZopeVersion(),
                         "Development/Unknown (2004.04.30.04.00.00)")

    def test_ZopeVersion_cvstag(self):
        self.prepare(None, "Nsome-tag")
        zope_version = self._Test__new()
        self.assertEqual(zope_version.getZopeVersion(),
                         "Development/Unknown (some-tag)")

    def test_ZopeVersion_cvsbranchtag(self):
        self.prepare(None, "Tsome-tag")
        zope_version = self._Test__new()
        self.assertEqual(zope_version.getZopeVersion(),
                         "Development/Unknown (some-tag)")

    def test_ZopeVersion_release(self):
        self.prepare("Zope X3 1.0.1a1", None)
        zope_version = self._Test__new()
        self.assertEqual(zope_version.getZopeVersion(),
                         "Zope X3 1.0.1a1")

    def test_ZopeVersion_release_cvsdate(self):
        # demonstrate that the version.txt data is discarded if
        # there's revision-control metadata:
        self.prepare("Zope X3 1.0.1a1", "D2004.04.30.04.00.00")
        zope_version = self._Test__new()
        self.assertEqual(zope_version.getZopeVersion(),
                         "Development/Unknown (2004.04.30.04.00.00)")

    def test_ZopeVersion_release_cvstag(self):
        # demonstrate that the version.txt data is discarded if
        # there's revision-control metadata:
        self.prepare("Zope X3 1.0.1a1", "Nsome-tag")
        zope_version = self._Test__new()
        self.assertEqual(zope_version.getZopeVersion(),
                         "Development/Unknown (some-tag)")

    def test_ZopeVersion_release_cvsbranchtag(self):
        # demonstrate that the version.txt data is discarded if
        # there's revision-control metadata:
        self.prepare("Zope X3 1.0.1a1", "Tsome-tag")
        zope_version = self._Test__new()
        self.assertEqual(zope_version.getZopeVersion(),
                         "Development/Unknown (some-tag)")


def test_suite():
    return unittest.makeSuite(Test)

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
