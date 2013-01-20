#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-html-xsl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.remove("/usr/bin/docbook2texi")
    pisitools.remove("/usr/bin/docbook2man")
    pisitools.remove("/usr/share/man/man1/docbook2texi.1")
    pisitools.remove("/usr/share/man/man1/docbook2man.1")

    pisitools.dodoc("AUTHORS", "TODO", "ChangeLog", "COPYING", "README", "NEWS", "THANKS")
