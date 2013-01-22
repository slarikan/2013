#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="icu/source"

def setup():
    autotools.autoconf("-f")
    options = "--with-data-packaging=library --disable-samples"
    if get.buildTYPE() == "_emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/_emul32/bin \
                     --sbindir=/_emul32/sbin"
    autotools.configure(options)
    pisitools.dosed("config/mh-linux", "-nodefaultlibs -nostdlib")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    if get.buildTYPE() == "_emul32":
        pisitools.domove("/_emul32/bin/icu-config", "/usr/bin", "icu-config-32")
        pisitools.removeDir("/_emul32")
        return
    
    pisitools.dohtml("../*.html")
