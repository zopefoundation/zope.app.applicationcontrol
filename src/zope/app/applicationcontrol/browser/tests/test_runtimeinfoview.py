##############################################################################
#
# Copyright (c) 2001, 2002, 2003 Zope Foundation and Contributors.
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
"""Runtime View tests

"""
import unittest

from zope.app.applicationcontrol.applicationcontrol import (
    applicationController)
from zope.app.applicationcontrol.runtimeinfo import RuntimeInfo
from zope.app.applicationcontrol.browser.runtimeinfo import RuntimeInfoView
from zope.app.applicationcontrol.interfaces import \
    IApplicationControl, IRuntimeInfo
from zope.component.testing import PlacelessSetup as PlacefulSetup

import zope.component

stypes = list, tuple


def provideAdapter(required, provided, factory, name='', **kw):

    gsm = zope.component.getGlobalSiteManager()

    assert not isinstance(required, stypes)
    required = (required,)

    gsm.registerAdapter(factory, required, provided, name, event=False)


class Test(PlacefulSetup, unittest.TestCase):

    def _TestView__newView(self, container):
        view = RuntimeInfoView()
        view.context = container
        view.request = None
        return view

    def test_RuntimeInfoView(self):
        provideAdapter(IApplicationControl, IRuntimeInfo, RuntimeInfo)
        test_runtimeinfoview = self._TestView__newView(applicationController)

        test_format = test_runtimeinfoview.runtimeInfo()
        self.assertIsInstance(test_format, dict)

        assert_keys = [
            'ZopeVersion', 'PythonVersion', 'PythonPath',
            'SystemPlatform', 'PreferredEncoding', 'FileSystemEncoding',
            'CommandLine', 'ProcessId', 'Uptime', 'DeveloperMode'
        ]
        test_keys = test_format.keys()

        self.assertEqual(sorted(assert_keys), sorted(test_keys))

        self.assertEqual("Unavailable", test_format["ZopeVersion"])

    def test_RuntimeInfoFailureView(self):
        test_runtimeinfoview = self._TestView__newView(applicationController)

        test_format = test_runtimeinfoview.runtimeInfo()
        self.assertIsInstance(test_format, dict)

        assert_keys = [
            'ZopeVersion',
            'PythonVersion',
            'PythonPath',
            'SystemPlatform',
            'PreferredEncoding',
            'FileSystemEncoding',
            'CommandLine',
            'ProcessId',
            'Uptime',
            'DeveloperMode']
        test_keys = test_format.keys()

        self.assertEqual(sorted(assert_keys), sorted(test_keys))

        for key in assert_keys:
            self.assertEqual("Unavailable", test_format[key])


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
