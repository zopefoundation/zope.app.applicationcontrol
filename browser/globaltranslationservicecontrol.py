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

$Id: globaltranslationservicecontrol.py,v 1.2 2004/03/06 16:50:12 jim Exp $
"""

from zope.app.applicationcontrol.interfaces import IGlobalTSControl

from zope.app.i18n import ZopeMessageIDFactory as _

class GlobalTSControlView:

    def getCatalogsInfo(self):
        globaltscontrol = IGlobalTSControl(self.context)
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
            globaltscontrol = IGlobalTSControl(self.context)
            catalogs = globaltscontrol.getCatalogsInfo()
            catalogNames = catalogs[(language,domain)]
            globaltscontrol.reloadCatalogs(catalogNames)
            status = _('message catalog successfully reloaded.')
        return status
