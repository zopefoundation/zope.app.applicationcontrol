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
"""Zope Version Tests

"""
import os

import shutil
import tempfile
import unittest

from zope.interface.verify import verifyObject
from zope.applicationcontrol.interfaces import IZopeVersion
from zope.app.applicationcontrol.zopeversion import ZopeVersion

class Test(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="test-zopeversion-")
        self.zopeVersion = ZopeVersion(self.tmpdir)

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def prepare(self, version):
        if version:
            with open(os.path.join(self.tmpdir, "version.txt"), "w") as f:
                f.write(version)
                if not version.endswith("\n"):
                    f.write("\n")

    def test_IVerify(self):
        verifyObject(IZopeVersion, self.zopeVersion)

    def test_ZopeVersion(self):
        self.prepare(None)
        self.assertEqual(self.zopeVersion.getZopeVersion(),
            "Development/Unknown")

    def test_ZopeVersion_release(self):
        self.prepare("Zope 3 1.0.0")
        self.assertEqual(self.zopeVersion.getZopeVersion(),
                         "Zope 3 1.0.0")

    def test_ZopeVersion_no_path_specified(self):
        zopeVersion = ZopeVersion(None)
        self.assertEqual(zopeVersion.result, "Meaningless")

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
