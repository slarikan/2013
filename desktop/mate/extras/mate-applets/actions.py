#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
			 --sysconfdir=/etc \
			 --localstatedir=/var \
			 --libexecdir=/usr/lib/mate-applets \
			 --disable-static \
			 --disable-scrollkeeper \
			 --disable-cpufreq \
			 --enable-polkit \
			 --enable-networkmanager \
			 --enable-mixer-applet \
			 --enable-mini-commander \
			 --enable-frequency-selector \
			 --enable-ipv6 \
			 --without-hal \
			 --disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")
