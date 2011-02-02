#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM-UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s" prefix="/usr"' % get.installDIR())

    pisitools.dodoc("README", "AUTHORS", "COPYING", "ChangeLog")
