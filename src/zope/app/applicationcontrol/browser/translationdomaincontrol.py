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
"""Server Control View

"""
__docformat__ = 'restructuredtext'

import zope.component
from zope.i18n.interfaces import ITranslationDomain

from zope.app.applicationcontrol.i18n import ZopeMessageFactory as _


class TranslationDomainControlView(object):

    def getCatalogsInfo(self):
        info = []
        for name, domain in zope.component.getUtilitiesFor(ITranslationDomain):
            if not hasattr(domain, 'getCatalogsInfo'):
                continue  # pragma: no cover
            lang_info = []
            info.append({'domain': name, 'languagesInfo': lang_info})
            for language, fileNames in domain.getCatalogsInfo().items():
                lang_info.append({'language': language,
                                  'fileNames': fileNames})
        return info

    def reloadCatalogs(self):
        """Do the reloading !"""
        status = ''

        if 'RELOAD' in self.request:
            language = self.request.get('language')
            domain = self.request.get('domain')

            domain = zope.component.getUtility(ITranslationDomain, domain)
            for lang, fileNames in domain.getCatalogsInfo().items():
                if lang == language:
                    domain.reloadCatalogs(fileNames)

            status = _('Message Catalog for ${language} language'
                       ' in ${domain} domain successfully reloaded.',
                       mapping={u'language': language,
                                u'domain': domain.domain})

        return status
