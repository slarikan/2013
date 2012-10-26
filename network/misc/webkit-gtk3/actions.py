#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "webkitgtk-%s" % get.srcVERSION()
shelltools.export("HOME", get.workDIR())
shelltools.export("XDG_DATA_HOME",  get.workDIR())

def setup():
    autotools.configure("--enable-dependency-tracking \
                         --disable-silent-rules \
                         --enable-introspection \
                         --with-gstreamer=0.10 \
                         --enable-filters \
                         --with-font-backend=pango \
                         --with-unicode-backend=icu \
                         --libexecdir=/usr/lib/webkitgtk3 \
                         --with-gtk=3.0 \
                         --enable-gtk-doc")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())
