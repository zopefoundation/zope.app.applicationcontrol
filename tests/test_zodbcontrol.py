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

$Id: test_zodbcontrol.py,v 1.2 2003/08/26 16:22:31 fdrake Exp $
"""
import unittest
import os

from zodb.storage.file import FileStorage
from zodb.db import DB
from zope.app.applicationcontrol import tests
from zope.app.applicationcontrol.zodbcontrol import ZODBControl
from zope.app.applicationcontrol.applicationcontrol import applicationController


class Test(unittest.TestCase):

    def setUp(self):
        db_file = os.path.join(os.path.dirname(tests.__file__), 'zodb.fs')
        self.storage = FileStorage(db_file)
        self.db = DB(self.storage, '')
        self.control = ZODBControl(applicationController)

    def tearDown(self):
        self.db.close()
        self.storage.cleanup()

    def test_getDatabaseSize(self):
        self.assertEqual(self.control.getDatabaseSize(self.db), 1183)


def test_suite():
    return unittest.makeSuite(Test)

if __name__ == '__main__':
    unittest.main()
