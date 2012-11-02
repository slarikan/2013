#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    if get.buildTYPE() == "emul32":
        options = " --prefix=/emul32 \
                    --libdir=/usr/lib32 \
                    --with-module-path=/usr/lib32/pkcs11"

        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
    else: options = " --with-module-path=/usr/lib/pkcs11"

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")
        pisitools.dosed("%s/usr/lib32/pkgconfig/p11-kit-1.pc" % get.installDIR(), "^(prefix=\/)emul32", r"\1usr")
    else: pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
