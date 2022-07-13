=======
CHANGES
=======

4.1.0 (2022-07-13)
------------------

- Add support for Python 3.7, 3.8, 3.9, 3.10.

- Drop support for Python 3.3 and 3.4.

- Make tests compatible with ``zope.app.locales >= 4.2``.


4.0.0 (2017-05-03)
------------------

- Add support for Python 3.4, 3.5 and 3.6 and PyPy.

- Remove test dependency on ``zope.app.testing`` and
  ``zope.app.zcmlfiles``, among others.

- Change dependency on ``ZODB3`` to ``ZODB``.

- Remove the ability of ``ZopeVersion``  to parse information from a
  subversion checkout. zope.app packages are in git now.

3.5.10 (2011-11-02)
-------------------

- Extended the locale-specific fix from version 3.5.6 for hosts
  which set ``LC_*`` in the environment:  those variables shadow ``LANG``.

- Replaced a testing dependency on zope.app.authentication with
  zope.password.

- Removed unneeded zope.app.appsetup test dependency.


3.5.9 (2010-12-18)
------------------

- Bugfix: AttributeError: 'module' object has no attribute '__file__'
  when you used ``pip install`` instead of ``easy_install``.

  The IZopeVersion utility now returns "Meaningless", since there's no
  monolithic Zope 3 in the modern eggified world.


3.5.8 (2010-09-17)
------------------

- Replaced a testing dependency on zope.app.securitypolicy with one on
  zope.securitypolicy.


3.5.7 (2010-07-08)
------------------

- 3.5.6 was a bad egg release.


3.5.6 (2010-07-07)
------------------

- Bugfix: Launching ``svn`` replaced the whole environment instead of just
  appending ``LANG``.


3.5.5 (2010-01-09)
------------------

- Extracted RuntimeInfo and ApplicationRoot functionality into
  zope.applicationcontrol. Import this functionality from this package
  instead (see BBB imports inside this package).

3.5.4 (2010-01-08)
------------------

- Test dependency on zptpage removed.


3.5.3 (2010-01-05)
------------------

- Updated to use newer zope.publisher 3.12 and zope.login to make
  tests work.


3.5.2 (2009-12-19)
------------------

- Move 'zope.ManageApplication' permission from zope.app.security package

- Break dependency on ``zope.app.appsetup`` by using a conditional import


3.5.1 (2009-08-15)
------------------

- Added missing (normal and test) dependencies.

- Renenabled functional tests.

3.5.0 (2009-05-23)
------------------

- The application controller is now registered as a utility so that other
  packages like zope.traversing and zope.app.publication do not need
  to depend on this package directly.  This also makes the application
  controller pluggable.

3.4.3 (2008-07-30)
------------------

- Make the test for the ZopeVersion bugfix in 3.4.2 not fail when run from an
  egg rather than a checkout.

3.4.2 (2008-07-30)
------------------

- Substitute zope.app.zapi by direct calls to its wrapped apis.
  See http://launchpad.net/bugs/219302

- Bugfix: ZopeVersion used to report an unknown version when running on a
  machine with a locale different than English.
  See http://launchpad.net/bugs/177733

- Fixed deprecation warning in ftesting.zcml: import ZopeSecurityPolicy from
  the new location.

3.4.1 (2007-09-27)
------------------

- rebumped to replace faulty egg

3.4.0 (2007-09-25)
------------------

- Initial documented release

- Reflect changes form zope.app.error refactoring
