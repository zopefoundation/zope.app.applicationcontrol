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
"""ZODB Control Tests

"""
import doctest
import unittest

import ZODB.MappingStorage
from ZODB.interfaces import IDatabase
from zope.testing import cleanup

from zope import component
from zope.app.applicationcontrol.browser.zodbcontrol import ZODBControlView
from zope.app.applicationcontrol.testing import ApplicationControlLayer


class TestZODBControlView(cleanup.CleanUp,
                          unittest.TestCase):

    def test_returns_status(self):

        view = ZODBControlView(None, None)
        view.status = self

        self.assertIs(self, view.update())

    def test_invalid_days(self):
        class MockRequest:
            def __init__(self, **kwargs):
                self.form = kwargs

        view = ZODBControlView(None,
                               MockRequest(
                                   days='not an int',
                                   PACK=True))

        result = view.update()
        self.assertEqual(['Error: Invalid Number'], result)

        del view.request.form['PACK']
        result = view.update()
        self.assertEqual(['Error: Invalid Number'], result)

    def test_pack_error(self):
        from ZODB.POSException import StorageError

        class Database:
            def pack(self, days=None):
                raise StorageError()

        component.provideUtility(Database(), IDatabase)

        class MockRequest:
            def __init__(self, **kwargs):
                self.form = kwargs

        view = ZODBControlView(None,
                               MockRequest(PACK=True, dbs=['']))

        result = view.update()

        result, = result
        self.assertEqual('ERROR packing ZODB "${name}": ${err}', result)
        self.assertEqual('', result.mapping['name'])
        self.assertIn('err', result.mapping)


def setUp(test):
    test.databases = test.globs['getRootFolder']()._p_jar.db().databases
    ZODB.MappingStorage.DB(databases=test.databases, database_name='2')

    for name, db in test.databases.items():
        component.provideUtility(db, IDatabase, name=name)


def tearDown(test):
    for db in test.databases.values():
        db.close()
    cleanup.cleanUp()


def test_suite():
    suite = unittest.TestSuite()
    zodb = doctest.DocFileSuite(
        'zodb.rst',
        setUp=setUp,
        tearDown=tearDown,
        globs={'getRootFolder': ApplicationControlLayer.getRootFolder})
    zodb.layer = ApplicationControlLayer
    suite.addTest(zodb)
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName(__name__))
    return suite
