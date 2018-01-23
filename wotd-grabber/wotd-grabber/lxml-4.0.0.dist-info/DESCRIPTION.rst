lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

To contact the project, go to the `project home page
<http://lxml.de/>`_ or see our bug tracker at
https://launchpad.net/lxml

In case you want to use the current in-development version of lxml,
you can get it from the github repository at
https://github.com/lxml/lxml .  Note that this requires Cython to
build the sources, see the build instructions on the project home
page.  To the same end, running ``easy_install lxml==dev`` will
install lxml from
https://github.com/lxml/lxml/tarball/master#egg=lxml-dev if you have
an appropriate version of Cython installed.


After an official release of a new stable series, bug fixes may become
available at
https://github.com/lxml/lxml/tree/lxml-4.0 .
Running ``easy_install lxml==4.0bugfix`` will install
the unreleased branch state from
https://github.com/lxml/lxml/tarball/lxml-4.0#egg=lxml-4.0bugfix
as soon as a maintenance branch has been established.  Note that this
requires Cython to be installed at an appropriate version for the build.

4.0.0 (2017-09-17)
==================

Features added
--------------

* The ElementPath implementation is now compiled using Cython,
  which speeds up the ``.find*()`` methods quite significantly.

* The modules ``lxml.builder``, ``lxml.html.diff`` and ``lxml.html.clean``
  are also compiled using Cython in order to speed them up.

* ``xmlfile()`` supports async coroutines using ``async with`` and ``await``.

* ``iterwalk()`` has a new method ``skip_subtree()`` that prevents walking into
  the descendants of the current element.

* ``RelaxNG.from_rnc_string()`` accepts a ``base_url`` argument to
  allow relative resource lookups.

* The XSLT result object has a new method ``.write_output(file)`` that serialises
  output data into a file according to the ``<xsl:output>`` configuration.

Bugs fixed
----------

* GH#251: HTML comments were handled incorrectly by the soupparser.
  Patch by mozbugbox.

* LP#1654544: The html5parser no longer passes the ``useChardet`` option
  if the input is a Unicode string, unless explicitly requested.  When parsing
  files, the default is to enable it when a URL or file path is passed (because
  the file is then opened in binary mode), and to disable it when reading from
  a file(-like) object.

  Note: This is a backwards incompatible change of the default configuration.
  If your code parses byte strings/streams and depends on character detection,
  please pass the option ``guess_charset=True`` explicitly, which already worked
  in older lxml versions.

* LP#1703810: ``etree.fromstring()`` failed to parse UTF-32 data with BOM.

* LP#1526522: Some RelaxNG errors were not reported in the error log.

* LP#1567526: Empty and plain text input raised a TypeError in soupparser.

* LP#1710429: Uninitialised variable usage in HTML diff.

* LP#1415643: The closing tags context manager in ``xmlfile()`` could continue
  to output end tags even after writing failed with an exception.

* LP#1465357: ``xmlfile.write()`` now accepts and ignores None as input argument.

* Compilation under Py3.7-pre failed due to a modified function signature.

Other changes
-------------

* The main module source files were renamed from ``lxml.*.pyx`` to plain
  ``*.pyx`` (e.g. ``etree.pyx``) to simplify their handling in the build
  process.  Care was taken to keep the old header files as fallbacks for
  code that compiles against the public C-API of lxml, but it might still
  be worth validating that third-party code does not notice this change.




