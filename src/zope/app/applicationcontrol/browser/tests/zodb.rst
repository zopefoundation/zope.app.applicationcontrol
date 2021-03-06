=================
ZODB Control View
=================

We provide default views which are relevant for administering mount points.

  >>> from zope.testbrowser.wsgi import Browser
  >>> browser = Browser()
  >>> browser.addHeader('Authorization','Basic mgr:mgrpw')
  >>> browser.handleErrors = False

  >>> browser.open('http://localhost/++etc++process/@@ZODBControl.html')

All registered databases are displayed. Each database can be packed by
selecting the according checkbox. Let us select the second database now:

  >>> browser.getControl(name='dbs:list').value = ['2']

Now we define to pack the database back to 7 days:

  >>> browser.getControl(name='days').value = '7'

Finally let's submit the form and start packing the database:

  >>> browser.getControl(name='PACK').click()
  >>> 'ZODB "2" successfully packed.' in browser.contents
  True
