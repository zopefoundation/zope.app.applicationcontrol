#
# This file is necessary to make this directory a package.

from zope.interface import implementer
from zope.applicationcontrol.interfaces import IServerControl


@implementer(IServerControl)
class MockServerControl(object):

    did_restart = None
    did_shutdown = None

    def restart(self, time):
        self.did_restart = time

    def shutdown(self, time):
        self.did_shutdown = time
