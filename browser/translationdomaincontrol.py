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

$Id: translationdomaincontrol.py,v 1.1 2004/03/08 23:33:39 srichter Exp $
"""
from zope.app.applicationcontrol.interfaces import ITranslationDomainControl
from zope.app.i18n import ZopeMessageIDFactory as _

class TranslationDomainControlView:

    def getCatalogsInfo(self):
        control = ITranslationDomainControl(self.context)
        return control.getCatalogsInfo()


    def reloadCatalogs(self):
        """Do the reloading !"""
        status = ''
        
        if 'RELOAD' in self.request:
            language = self.request.get('language')
            domain = self.request.get('domain')
            control = ITranslationDomainControl(self.context)
            control.reloadCatalogs(domain, language)
            status = _('Message Catalog successfully reloaded.')
        return status
