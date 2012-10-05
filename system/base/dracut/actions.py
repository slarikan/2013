#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    shelltools.export("PYTHONDONTWRITEBYTECODE","1")
    autotools.rawInstall("prefix=/usr \
                          libdir=/usr/lib \
                          sysconfdir=/etc \
                          mandir=/usr/share/man \
                          DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/logrotate.d", "dracut.logrotate")
    pisitools.dosym("/usr/bin/dracut","/sbin/dracut")
    
    pisitools.dodoc("AUTHORS", "COPYING", "README*", "NEWS", "TODO",
                    "HACKING", "dracut.html", "dracut.png", "dracut.svg")
