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
"""Zope Version Tests

$Id: test_zopeversion.py,v 1.7 2004/05/03 14:18:25 fdrake Exp $
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

    def test_ZopeVersion(self):
        self.prepare(None, None)
        zope_version = self._Test__new()
        self.assertEqual(zope_version.getZopeVersion(), "Development/Unknown")

    def test_ZopeVersion_cvstag(self):
        self.prepare(None, "Tsome-tag")
        zope_version = self._Test__new()
        self.assertEqual(zope_version.getZopeVersion(),
                         "Development/Unknown (some-tag)")

    def test_ZopeVersion_release(self):
        self.prepare("Zope X3 1.0.1a1", None)
        zope_version = self._Test__new()
        self.assertEqual(zope_version.getZopeVersion(),
                         "Zope X3 1.0.1a1")

    def test_ZopeVersion_release_cvstag(self):
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
