##############################################################################
#
# Copyright (c) 2003 Zope Corporation and Contributors.
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
"""Translation Domain Control

$Id: translationdomaincontrol.py,v 1.1 2004/03/08 23:33:38 srichter Exp $
"""
from zope.interface import implements
from zope.app import zapi
from zope.i18n.interfaces import ITranslationDomain
from zope.app.applicationcontrol.interfaces import \
     IApplicationControl, ITranslationDomainControl

class TranslationDomainControl:
    implements(ITranslationDomainControl)
    __used_for__ = IApplicationControl

    def __init__(self, context):
        self.context = context

    def getCatalogsInfo(self):
        """See .interfaces.ITranslationDomainControl"""
        info = []
        for name, domain in zapi.getUtilitiesFor(None, ITranslationDomain):
            if not hasattr(domain, 'getCatalogsInfo'):
                continue
            for language, fileNames in domain.getCatalogsInfo().items():
                info.append({'domain': name,
                             'language': language,
                             'fileNames': fileNames})
        return info
                

    def reloadCatalogs(self, domain, language):
        """See .interfaces.ITranslationDomainControl"""
        domain = zapi.getUtility(None, ITranslationDomain, domain)
        for lang, fileNames in domain.getCatalogsInfo().items():
            if lang == language:
                domain.reloadCatalogs(fileNames)

