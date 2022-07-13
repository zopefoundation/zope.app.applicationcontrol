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
"""Server Control View Tests

"""
import unittest

import zope.component
from zope.component.testing import PlacelessSetup as PlacefulSetup

from zope.app.applicationcontrol.applicationcontrol import \
    applicationController
from zope.app.applicationcontrol.browser.servercontrol import ServerControlView
from zope.app.applicationcontrol.interfaces import IServerControl
from zope.app.applicationcontrol.tests import MockServerControl


class Test(PlacefulSetup, unittest.TestCase):

    def _TestView__newView(self, container, request):
        view = ServerControlView()
        view.context = container
        view.request = request
        return view

    def test_ServerControlView(self):
        control = MockServerControl()
        globalSiteManager = zope.component.getGlobalSiteManager()
        globalSiteManager.registerUtility(control, IServerControl)

        test_serverctrl = self._TestView__newView(
            applicationController,
            {'shutdown': 1,
             'time': 100},
        )
        test_serverctrl.action()
        self.assertEqual(control.did_shutdown, 100)

        test_serverctrl = self._TestView__newView(
            applicationController,
            {'restart': 1,
             'time': 100},
        )
        test_serverctrl.action()
        self.assertEqual(control.did_restart, 100)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
