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
"""Register ServerControl configuration directives.

$Id: metadirectives.py,v 1.1 2003/08/03 21:22:29 philikon Exp $
"""

from zope.interface import Interface
from zope.configuration.fields import GlobalObject
from zope.schema import Float, TextLine

class IRegisterShutdownHookDirective(Interface):
    """
    Register a shutdown hook
    """

    call = GlobalObject(
        title=u"Callable",
        description=u"""
        Callable that takes no arguments and invokes the shutdown""",
        required=True
        )

    priority = Float(
        title=u"Priority",
        required=True
        )

    name = TextLine(
        title=u"Name",
        required=False
        )
