import unittest

from webtest import TestApp
from zope.component import getUtility
from zope.error.interfaces import IErrorReportingUtility
from zope.publisher.browser import BrowserView
from zope.traversing.browser.absoluteurl import absoluteURL

from zope.app.applicationcontrol.testing import ApplicationControlLayer


class BrowserTestCase(unittest.TestCase):

    layer = ApplicationControlLayer

    def setUp(self):
        super(BrowserTestCase, self).setUp()
        self._testapp = TestApp(self.layer.make_wsgi_app())

    def publish(self, path, basic=None, form=None, headers=None):
        assert basic
        self._testapp.authorization = ('Basic', tuple(basic.split(':')))

        env = {'wsgi.handleErrors': False}
        if form:
            response = self._testapp.post(path, params=form,
                                          extra_environ=env, headers=headers)
        else:
            response = self._testapp.get(
                path, extra_environ=env, headers=headers)
        return response


class ErrorRedirect(BrowserView):
    # copied from zope.app.error
    def action(self):
        # Some locations (eg ++etc++process) throw a TypeError exception when
        # finding their absoluteurl, if this happens catch the error and
        # redirect the browser to the site root "/@@errorRedirect.html"
        # to handle redirection to the site error logger instead
        try:
            err = getUtility(IErrorReportingUtility)
            url = absoluteURL(err, self.request)
        except TypeError:
            url = self.request.getApplicationURL() + "/@@errorRedirect.html"
        else:
            # The real zope.app.error would redirect to
            # url + @@SelectedManagementView.html
            raise NotImplementedError()

        self.request.response.redirect(url)
