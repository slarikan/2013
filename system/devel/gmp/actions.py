#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    # FIXME: check if we need sse2 libs too, if yes recompile in different dir and put in prefix/lib/sse2
    #~ shelltools.export("CCAS","%s -c -Wa,--noexecstack" % get.CC())

    options = "--enable-cxx \
               --enable-mpbsd \
               --enable-fft \
               --localstatedir=/var/state/gmp"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32"

        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("ABI", "32")

    autotools.configure(options)

def build():
    autotools.make()

#~ def check():
    #~ autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")
        return

    pisitools.doinfo("doc/*info*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYING.LIB", "NEWS", "README")
