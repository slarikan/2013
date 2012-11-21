#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
WorkDir="qpopper4.1.0"

def setup():
    autotools.configure("--enable-64-bit --enable-spool-dir=/var/spool/clientmqueue")

def build():
    autotools.make()

def install():
    autotools.install()

    #pisitools.removeDir("/usr/share")

    #pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "doc/liblink", "doc/libroutines")
