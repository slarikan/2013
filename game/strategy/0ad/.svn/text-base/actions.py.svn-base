#!/usr/bin/python
# -*- coding: utf-8 -*-


from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "0ad-r10803-alpha"

def setup():
    #thanks to s.dalgic
    shelltools.export("pardusCC", get.CC())
    shelltools.export("pardusCXX", get.CXX())
    shelltools.export("pardusCFLAGS", get.CXX())
    shelltools.export("pardusCPPFLAGS", get.CXXFLAGS())
    
    shelltools.cd("build/workspaces/")
    shelltools.system("./update-workspaces.sh \
                        --with-system-enet \
                        JOBS=%s" % get.makeJOBS())

def build():
    shelltools.cd("build/workspaces/gcc")
    autotools.make("CONFIG=Release")

def install():
    pisitools.dodoc("LICENSE.txt","license_dbghelp.txt","license_gpl-2.0.txt","license_lgpl-2.1.txt","README.txt",)
    pisitools.insinto("/opt/0ad","binaries/*")

