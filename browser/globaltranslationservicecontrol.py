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
""" Server Control View

$Id: globaltranslationservicecontrol.py,v 1.1 2004/03/01 13:43:25 philikon Exp $
"""

from zope.app.applicationcontrol.interfaces import IGlobalTSControl
from zope.component import getAdapter

from zope.app.i18n import ZopeMessageIDFactory as _

class GlobalTSControlView:

    def getCatalogsInfo(self):
        globaltscontrol = getAdapter(self.context, IGlobalTSControl)
        catalogsInfo = globaltscontrol.getCatalogsInfo()
        languages_domains = catalogsInfo.keys()
        domains_languages = []
        for language, domain in languages_domains:
          domains_languages.append((domain, language))
        domains_languages.sort() 
        catalogsInfoMaps = []
        for domain, language in domains_languages:
            fileNames = list(catalogsInfo[(language, domain)])
            catalogsInfoMaps.append({'language':language, 'domain':domain,
                                     'fileNames':fileNames})
        return catalogsInfoMaps


    def reloadCatalogs(self):
        """Do the reloading !"""
        status = ''
        
        if 'RELOAD' in self.request:
            language = self.request.get('language')
            domain = self.request.get('domain')
            globaltscontrol = getAdapter(self.context, IGlobalTSControl)
            catalogs = globaltscontrol.getCatalogsInfo()
            catalogNames = catalogs[(language,domain)]
            globaltscontrol.reloadCatalogs(catalogNames)
            status = _('message catalog successfully reloaded.')
        return status
