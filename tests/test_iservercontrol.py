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

$Id: test_iservercontrol.py,v 1.2 2002/12/25 14:12:26 jim Exp $
"""

from unittest import TestCase, TestSuite, main, makeSuite
from zope.interface.verify import verifyObject

from zope.app.interfaces.applicationcontrol.servercontrol import \
 IServerControl, DoublePriorityError, NotCallableError


#############################################################################
# If your tests change any global registries, then uncomment the
# following import and include CleanUp as a base class of your
# test. It provides a setUp and tearDown that clear global data that
# has registered with the test cleanup framework.  Don't use this
# tests outside the Zope package.

# from zope.testing.cleanup import CleanUp # Base class w registry cleanup

#############################################################################

def stub_callback():
    """stupid callable object"""
    pass

class BaseTestIServerControl:
    """Base test cases for ServerControllers.

       Subclasses need to define a method, '_Test__new', that
       takes no arguments and that returns a new empty test ServerController.
    """

    ############################################################
    # Interface-driven tests:

    def test_IVerify(self):
        verifyObject(IServerControl, self._Test__new())

    def test_registerShutdownHook(self):
        server_control = self._Test__new()

        # Try to register a noncallable object
        self.assertRaises(NotCallableError,
              server_control.registerShutdownHook, None, 10, "test")

        # Try to register a priority for a second time
        server_control.registerShutdownHook(stub_callback, 10, "Test")
        self.assertRaises(DoublePriorityError,
              server_control.registerShutdownHook, stub_callback, 10, "test2")

class Test(BaseTestIServerControl, TestCase):
    def _Test__new(self):
        from zope.app.applicationcontrol.servercontrol \
           import ServerControl
        return ServerControl()

def test_suite():
    return makeSuite(Test)

if __name__=='__main__':
    main(defaultTest='test_suite')
