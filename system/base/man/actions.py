#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


WorkDir="man-db-%s" % get.srcVERSION()

def setup():
    #who knows pisitools.dosed :)
    cmd="sed -i '/gets is a security hole/d' gnulib/lib/stdio.in.h"
    shelltools.system(cmd)
    autotools.configure("--disable-setuid \
                          --disable-rpath \
                          --docdir=/%s/%s \
                          --with-device=utf8 \
                          --with-config-file=/etc/man.conf \
                          --with-db=gdbm \
                          --enable-mb-groff" % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make("nls=all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README")
