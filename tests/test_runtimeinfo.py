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
##############################################################################
"""Runtime Info Tests

$Id: test_runtimeinfo.py,v 1.9 2004/03/24 11:13:15 hdima Exp $
"""
import unittest
import os, sys, time

try:
    import locale
except ImportError:
    locale = None

from zope.component import getService
from zope.interface import implements
from zope.interface.verify import verifyObject
from zope.app.applicationcontrol.applicationcontrol import applicationController
from zope.app.applicationcontrol.interfaces import IRuntimeInfo, IZopeVersion
from zope.app.site.tests.placefulsetup import PlacefulSetup

# seconds, time values may differ in order to be assumed equal
time_tolerance = 2
stupid_version_string = "3085t0klvn93850voids"

class TestZopeVersion:
    """A fallback implementation for the ZopeVersion utility."""

    implements(IZopeVersion)

    def getZopeVersion(self):
        return stupid_version_string

class Test(PlacefulSetup, unittest.TestCase):

    def _Test__new(self):
        from zope.app.applicationcontrol.runtimeinfo import RuntimeInfo
        return RuntimeInfo(applicationController)

    def _getPreferredEncoding(self):
        if locale is None:
            return sys.getdefaultencoding()
        return locale.getpreferredencoding()

    def _getFileSystemEncoding(self):
        enc = sys.getfilesystemencoding()
        if enc is None:
            enc = self._getPreferredEncoding()
        return enc

    def testIRuntimeInfoVerify(self):
        verifyObject(IRuntimeInfo, self._Test__new())

    def test_PreferredEncoding(self):
        runtime_info = self._Test__new()
        enc = self._getPreferredEncoding()
        self.assertEqual(runtime_info.getPreferredEncoding(), enc)

    def test_FileSystemEncoding(self):
        runtime_info = self._Test__new()
        enc = self._getFileSystemEncoding()
        self.assertEqual(runtime_info.getFileSystemEncoding(), enc)

    def test_ZopeVersion(self):
        runtime_info = self._Test__new()

        # we expect that there is no utility
        self.assertEqual(runtime_info.getZopeVersion(), "")

        getService(None,'Utilities').provideUtility(IZopeVersion,
                                               TestZopeVersion())
        self.assertEqual(runtime_info.getZopeVersion(),
                                         stupid_version_string)
    def test_PythonVersion(self):
        runtime_info = self._Test__new()
        enc = self._getPreferredEncoding()
        self.assertEqual(runtime_info.getPythonVersion(),
                unicode(sys.version, enc))

    def test_SystemPlatform(self):
        runtime_info = self._Test__new()
        test_platform = (sys.platform,)
        if hasattr(os, "uname"):
            test_platform = os.uname()
        enc = self._getPreferredEncoding()
        self.assertEqual(runtime_info.getSystemPlatform(),
                unicode(" ".join(test_platform), enc))

    def test_CommandLine(self):
        runtime_info = self._Test__new()
        self.assertEqual(runtime_info.getCommandLine(), " ".join(sys.argv))

    def test_ProcessId(self):
        runtime_info = self._Test__new()
        self.assertEqual(runtime_info.getProcessId(), os.getpid())

    def test_Uptime(self):
        runtime_info = self._Test__new()
        # whats the uptime we expect?

        start_time = applicationController.getStartTime()
        asserted_uptime = time.time() - start_time

        # get the uptime the current implementation calculates
        test_uptime = runtime_info.getUptime()

        self.failUnless(abs(asserted_uptime - test_uptime) < time_tolerance)


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(Test),
        ))

if __name__ == '__main__':
    unittest.main()
