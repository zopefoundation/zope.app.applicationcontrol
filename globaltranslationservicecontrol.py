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
"""ZODB Control

$Id: globaltranslationservicecontrol.py,v 1.1 2003/08/12 15:50:09 gotcha Exp $
"""
import os
from zope.interface import implements
from zope.app.interfaces.applicationcontrol import \
     IApplicationControl, IGlobalTSControl
from zope.i18n.globaltranslationservice import translationService

class GlobalTSControl:

    implements(IGlobalTSControl)
    __used_for__ = IApplicationControl

    def __init__(self, context):
        self.context = context

    def getCatalogsInfo(self):
        """See zope.app.interfaces.applicationControl.IGlobalTSControl"""
        return translationService.getCatalogsInfo()

    def reloadCatalogs(self, catalogName):
        """See zope.app.interfaces.applicationControl.IGlobalTSControl"""
        return translationService.reloadCatalogs(catalogName)

