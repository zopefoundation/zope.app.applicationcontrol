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
"""Translation Domain Control Tests

"""
import unittest

from zope.app.applicationcontrol.browser.tests import BrowserTestCase


class MessageCatalogControlTest(BrowserTestCase):

    def testDomainOverview(self):
        response = self.publish(
            '/++etc++process/@@TranslationDomain.html',
            basic='globalmgr:globalmgrpw')

        for link_name in ('servercontrol.html', '@@ZODBControl.html',
                          'index.html'):
            response.click(href=link_name,
                           extra_environ={'wsgi.handleErrors': False})

    def testReload(self):
        response = self.publish('/++etc++process/@@TranslationDomain.html',
                                basic='globalmgr:globalmgrpw',
                                form={'language': 'de',
                                      'domain': 'zope',
                                      'RELOAD': 'Reload'})
        body = response.unicode_normal_body
        self.assertIn('Message Catalog for de language in zope domain'
                      ' successfully reloaded.', body)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
