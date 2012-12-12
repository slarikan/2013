#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

shelltools.export("HOME", get.workDIR())

def setup():
    for (path, dirs, files) in os.walk(get.workDIR()):
        for file in files:
            if file.endswith(".c"):
                with open("%s/%s" % (path, file)) as f:
                    lines = f.readlines()
                new_file = ""
                for line in lines:
                    if not line.find("g_type_init()") == -1:
                        new_file = new_file + "#if !GLIB_CHECK_VERSION(2,35,0)\n" + line + "#endif\n"
                    else: 
                        new_file = new_file + line
                open("%s/%s" % (path, file), "w").write(new_file)
    autotools.autoreconf("-fvi")
    #autotools.autoconf("-f")
    autotools.configure()

def build():
    autotools.make()

"""
#Requires dbus-test-runner (https://launchpad.net/dbus-test-runner)

def check():
    autotools.make("check")
"""

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README", "NEWS")

    pisitools.removeDir("/usr/share/gtk-doc")
