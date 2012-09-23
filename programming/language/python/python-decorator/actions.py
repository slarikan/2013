#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def check():
    shelltools.system("nosetests --with-doctest -e documentation")

def install():
    pythonmodules.install()

    pisitools.dodoc("README.txt", "documentation.py")
