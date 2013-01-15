#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    # Fix sandbox violation
    pisitools.dosed("tools/pykdeuic4/CMakeLists.txt", "(\$\{BIN_INSTALL_DIR\}\/pykdeuic4)", r"%s/\1" % get.installDIR())
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()
