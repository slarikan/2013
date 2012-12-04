#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

yusuf = get.ARCH().replace("i686", "i386")

WorkDir = "%s/%s-%s-1661.%s.linux" % (get.ARCH(), get.srcNAME(), get.srcVERSION(), yusuf)

def install():
    shelltools.system("./install --prefix /usr --force --repackage %s/usr" % get.installDIR())

    pisitools.dosym("/usr/lib/browser-plugins/libflashplayer.so", "/usr/lib/opera/plugins/libflashplayer.so")
