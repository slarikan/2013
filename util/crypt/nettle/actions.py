#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    options = "--disable-static \
               --enable-shared"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32 \
                     --includedir=/usr/include"  #to have correct .pc
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
    else:
        options += " --libdir=/usr/lib"

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")
        pisitools.remove("/usr/lib32/*.a")
        pisitools.dosed("%s/usr/lib32/pkgconfig/nettle.pc" % get.installDIR(), "^(prefix=\/)emul32", r"\1usr")
        return
    pisitools.remove("/usr/lib/*.a")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README", "nettle.pdf")
