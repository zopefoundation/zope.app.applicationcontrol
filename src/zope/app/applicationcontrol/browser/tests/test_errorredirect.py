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
import unittest

from zope.app.applicationcontrol.browser.tests import BrowserTestCase


class ErrorRedirectTest(BrowserTestCase):

    def testErrorRedirect(self):
        response = self.publish('/++etc++process/@@errorRedirect.html',
                                basic='globalmgr:globalmgrpw')
        self.assertEqual('http://localhost/@@errorRedirect.html',
                         response.location)
        self.assertEqual(302, response.status_int)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
