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

def setup():
    shelltools.system("./autogen.sh --prefix=/usr \
				    --sysconfdir=/etc \
				    --localstatedir=/var \
				    --disable-static \
				    --disable-schemas-install \
				    --with-mateconf-source='xml::/etc/mateconf/mateconf.xml.defaults' \
				    --enable-sm") 
    autotools.configure("--disable-schemas-install \
    			 --disable-compositor")

def build():
    autotools.make()
    
def install():
    shelltools.makedirs("%s/etc/mateconf/mateconf.xml.defaults" % get.installDIR()) 
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    #remove marco-window-demo
    pisitools.remove("/usr/bin/marco-window-demo")
    #I hope Comar works
    #shelltools.export("MATECONF_CONFIG_SOURCE", "xml::"+ get.installDIR() +"/etc/mateconf/mateconf.xml.defaults")
    #shelltools.system("install -v -d -m755 "+ get.installDIR() +"/etc/mateconf/mateconf.xml.defaults")
    #shelltools.system("mateconftool-2 --makefile-install-rule "+ get.installDIR() +"/etc/mateconf/schemas/*.schemas")
    #shelltools.chmod(get.installDIR() +"/etc/mateconf", 0755)
    #install schemas like arch and debian
    #shelltools.makedirs("%s/usr/share/mateconf/schemas" % get.installDIR()) 
    #shelltools.system("mateconf-merge-schema "+ get.installDIR() +"/usr/share/mateconf/schemas/mate-window-manager.schemas --domain mate-window-manager "+ get.installDIR() +"/etc/mateconf/schemas/*.schemas")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

