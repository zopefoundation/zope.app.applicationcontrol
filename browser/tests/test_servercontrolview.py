##############################################################################
#
# Copyright (c) 2001, 2002, 2003 Zope Corporation and Contributors.
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
"""Server Control View Tests

$Id: test_servercontrolview.py,v 1.1 2004/03/01 13:43:25 philikon Exp $
"""
import unittest

from zope.app.applicationcontrol.applicationcontrol import applicationController
from zope.app.applicationcontrol.servercontrol import ServerControl
from zope.app.applicationcontrol.browser.servercontrol import ServerControlView
from zope.app.applicationcontrol.interfaces import IServerControl
from zope.app.services.servicenames import Utilities
from zope.app.services.tests.placefulsetup import PlacefulSetup
from zope.component import getService

class Test(PlacefulSetup, unittest.TestCase):

    def _TestView__newView(self, container, request):
        view = ServerControlView()
        view.context = container
        view.request = request
        return view

    def test_ServerControlView(self):
        getService(None,Utilities).provideUtility(
              IServerControl, ServerControl())

        test_serverctrl = self._TestView__newView(
            applicationController,
            {'shutdown': 1},
            )
        test_serverctrl.action()

        test_serverctrl = self._TestView__newView(
            applicationController,
            {'restart': 1},
            )
        test_serverctrl.action()


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(Test),
        ))

if __name__ == '__main__':
    unittest.main()
