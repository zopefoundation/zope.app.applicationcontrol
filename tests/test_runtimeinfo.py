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
"""

Revision information:
$Id: test_runtimeinfo.py,v 1.2 2002/12/25 14:12:26 jim Exp $
"""

from unittest import TestCase, TestSuite, main, makeSuite
from zope.interface.verify import verifyObject

import os, sys, time
from zope.component import getService
from zope.app.interfaces.applicationcontrol.runtimeinfo import IRuntimeInfo
from zope.app.applicationcontrol.applicationcontrol import \
  applicationController
from zope.app.interfaces.applicationcontrol.zopeversion import IZopeVersion

# seconds, time values may differ in order to be assumed equal
time_tolerance = 2
stupid_version_string = "3085t0klvn93850voids"

class TestZopeVersion:
    """A fallback implementation for the ZopeVersion utility."""

    __implements__ = IZopeVersion

    def getZopeVersion(self):
        return stupid_version_string

from zope.app.services.tests.placefulsetup\
           import PlacefulSetup

class Test(PlacefulSetup, TestCase):

    def _Test__new(self):
        from zope.app.applicationcontrol.runtimeinfo import RuntimeInfo
        return RuntimeInfo(applicationController)

    ############################################################
    # Interface-driven tests:

    def testIRuntimeInfoVerify(self):
        verifyObject(IRuntimeInfo, self._Test__new())

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
        self.assertEqual(runtime_info.getPythonVersion(), sys.version)

    def test_SystemPlatform(self):
        runtime_info = self._Test__new()
        test_platform = (sys.platform,)
        if hasattr(os, "uname"):
            test_platform = os.uname()
        self.assertEqual(runtime_info.getSystemPlatform(), test_platform)

    def test_CommandLine(self):
        runtime_info = self._Test__new()
        self.assertEqual(runtime_info.getCommandLine(), sys.argv)

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
    return makeSuite(Test)

if __name__=='__main__':
    main(defaultTest='test_suite')
