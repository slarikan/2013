#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

#WorkDir="OpenJPEG_v1_5"

def setup():
#    shelltools.system("rm -rf thirdparty")

#    shelltools.makedirs("build")
#    shelltools.cd("build")

#    cmaketools.configure("-DBUILD_EXAMPLES:BOOL=ON \
#                          -DBUILD_SHARED_LIBS:BOOL=ON \
#                          -DINCLUDE_INSTALL_DIR=/%s/include" % get.defaultprefixDIR(), sourceDir="..")

    autotools.configure("--disable-static --disable-silent-rules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("openjpeg/openjpeg.h", "/usr/include/openjpeg.h")

    pisitools.dodoc("README*")
