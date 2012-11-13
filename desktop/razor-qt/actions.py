#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/razorqt/work/ and:
WorkDir="razorqt-%s" % (get.srcVERSION())

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DENABLE_POLICYKIT=ON \
                          -DBUNDLE_XDG_UTILS=NO \
                          -DSYSCONF_INSTALL_DIR=/etc \
                          -DCMAKE_SKIP_RPATH=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("razorqt")

# You can use these as variables, they will replace GUI values before build.
# Package Name : razorqt
# Version : 0.5.0
# Summary : falan filan

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
