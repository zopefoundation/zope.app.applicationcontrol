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

$Id: test_applicationcontrol.py,v 1.3 2003/04/30 23:37:48 faassen Exp $
"""

from unittest import TestCase, main, makeSuite
from zope.interface.verify import verifyObject

import time
from zope.app.applicationcontrol.applicationcontrol import \
  ApplicationControl
from zope.app.interfaces.applicationcontrol.applicationcontrol import \
  IApplicationControl

# seconds, time values may differ in order to be assumed equal
time_tolerance = 2

#############################################################################
# If your tests change any global registries, then uncomment the
# following import and include CleanUp as a base class of your
# test. It provides a setUp and tearDown that clear global data that
# has registered with the test cleanup framework.  Don't use this
# tests outside the Zope package.

# from zope.testing.cleanup import CleanUp # Base class w registry cleanup

#############################################################################

class Test(TestCase):

    def _Test__new(self):
        return ApplicationControl()

    ############################################################
    # Interface-driven tests:

    def test_IVerify(self):
        verifyObject(IApplicationControl, self._Test__new())

    def test_startTime(self):
        assert_time = time.time()
        test_time = self._Test__new().getStartTime()

        self.failUnless(abs(assert_time - test_time) < time_tolerance)


def test_suite():
    return makeSuite(Test)

if __name__=='__main__':
    main(defaultTest='test_suite')
