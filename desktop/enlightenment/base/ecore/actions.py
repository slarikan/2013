#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -fvisibility=hidden" % get.CFLAGS())
shelltools.export("LDFLAGS", "%s -fvisibility=hidden" % get.LDFLAGS())

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --enable-glib \
                         --enable-ecore-evas \
                         --enable-ecore-con \
                         --enable-ecore-ipc \
                         --enable-ecore-file \
                         --enable-ecore-input \
                         --enable-ecore-imf \
                         --enable-ecore-x \
                         --enable-ecore-fb \
                         --disable-ecore-directfb \
                         --enable-ecore-evas-fb \
                         --enable-ecore-evas-directfb \
                         --enable-ecore-evas-software-buffer \
                         --enable-ecore-evas-software-x11 \
                         --enable-ecore-evas-xrender-x11 \
                         --enable-ecore-evas-opengl-x11 \
                         --enable-openssl \
                         --enable-inotify \
                         --enable-poll \
                         --enable-curl \
                         --disable-gnutls \
                         --with-x")
                         #--enable-ecore-directfb causes error for edje build

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/share")

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
