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
  
    shelltools.system("./autogen.sh --prefix=/usr --sysconfdir=/etc \
        --localstatedir=/var --libexecdir=/usr/bin \
        --with-mateconf-source='xml::/etc/mateconf/mateconf.xml.defaults' \
        --disable-static")
    autotools.configure()
    
    

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    #shelltools.export("MATECONF_CONFIG_SOURCE", "xml::"+ get.installDIR() +"/etc/mateconf/mateconf.xml.defaults")
    #shelltools.system("install -v -d -m755 "+ get.installDIR() +"/etc/mateconf/mateconf.xml.defaults")
    #shelltools.system("mateconftool-2 --makefile-install-rule "+ get.installDIR() +"/etc/mateconf/schemas/*.schemas")
    #shelltools.chmod(get.installDIR() +"/etc/mateconf", 0755) 
