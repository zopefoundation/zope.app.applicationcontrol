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
"""Application Control Interface

$Id: interfaces.py,v 1.3 2004/03/23 13:35:07 hdima Exp $
"""
from zope.interface import Interface

class ServerControlError(Exception):
    """Represents an error in the ServerControl."""

class DoublePriorityError(ServerControlError):
    """A second hook was registered for a priority."""

class NotCallableError(ServerControlError):
    """Raisen if a given object is not callable."""


class IApplicationControl(Interface):
    """The application control instance is usually generated upon startup and
    can therefore record the startup time."""

    def getStartTime():
        """Return time the application started in seconds since the epoch."""


class IRuntimeInfo(Interface):
    """ Runtime Information Adapter for Application Control """

    def getPreferredEncoding():
        """Return the encoding used for text data, according
           to user system preferences"""

    def getZopeVersion():
        """Return a string containing the descriptive version of the
           current zope installation"""

    def getPythonVersion():
        """Return an unicode string containing verbose description
           of the python interpreter"""

    def getPythonPath():
        """Return a tuple containing the lookup paths of the python interpreter
        """

    def getSystemPlatform():
        """Return an unicode string containing the system platform name
        """

    def getCommandLine():
        """Return the command line string Zope was invoked with"""

    def getProcessId():
        """Return the process id number currently serving the request
        """

    def getUptime():
        """Return the Zope server uptime in seconds."""


class IZopeVersion(Interface):
    """ Zope version """

    def getZopeVersion():
        """Return a string containing the Zope version (possibly including
           CVS information)"""


class IServerControl(Interface):
    """Defines methods for shutting down and restarting the server.

    This utility also keeps a registry of things to call when shutting down
    zope. You can register using this interface or the zcml on the global
    ServerController instance.
    """

    def shutdown():
        """Shutdown the server gracefully

        Returns: Nothing
        """

    def restart():
        """Restart the server gracefully

        Returns: Nothing
        """

    def registerShutdownHook(call, priority, name):
        """Register a function that will be callen on server shutdown.

        The function needs to takes no argument at all."""


class IZODBControl(Interface):
    """This control manages the state of the ZODB."""

    def getDatabaseSize(db):
        """Return the database size in bytes."""

    def pack(db, days):
        """Pack the ZODB. Remove all entries that are older than 'days' days."""


class ITranslationDomainControl(Interface):
    """This control manages the state of the translation service."""

    def getCatalogsInfo():
        """Return the registered languages."""

    def reloadCatalogs(domain, language):
        """reload the named catalogs from file"""

