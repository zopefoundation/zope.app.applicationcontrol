#
# This file is necessary to make this directory a package.

from zope.applicationcontrol.interfaces import IServerControl
from zope.interface import implementer


@implementer(IServerControl)
class MockServerControl:

    did_restart = None
    did_shutdown = None

    def restart(self, time):
        self.did_restart = time

    def shutdown(self, time):
        self.did_shutdown = time
