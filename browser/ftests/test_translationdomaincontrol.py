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
#
##############################################################################
"""Translation Domain Control Tests

$Id$
"""
import unittest
from zope.app.tests.functional import BrowserTestCase

class ZODBControlTest(BrowserTestCase):

    def testDomainOverview(self):
        response = self.publish(
            '/++etc++process/@@TranslationDomain.html',
            basic='mgr:mgrpw')

        body = response.getBody()
        self.checkForBrokenLinks(body,
                                 '/++etc++process/@@TranslationDomain.html',
                                 basic='mgr:mgrpw')
        
    def testReload(self):
        response = self.publish('/++etc++process/@@TranslationDomain.html',
                                basic='mgr:mgrpw',
                                form={'language': u'en',
                                      'domain': u'zope',
                                      'RELOAD': u'Reload'})
        body = response.getBody()
        self.assert_('Message Catalog successfully reloaded.' in body)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ZODBControlTest))
    return suite

if __name__=='__main__':
    unittest.main(defaultTest='test_suite')
