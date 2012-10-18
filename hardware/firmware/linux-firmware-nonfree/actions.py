#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "firmware-nonfreebox"

def install():
    pisitools.insinto("/lib/firmware", "*")

    # Remove installed WHENCE and LIC* files from /lib/firmware
    pisitools.remove("/lib/firmware/broadcom/BCM-LEGAL.txt")
    pisitools.remove("/lib/firmware/crystalhd/BOM")
    pisitools.remove("/lib/firmware/dvb/BOM")
    pisitools.remove("/lib/firmware/prism54_softmac/BOM")
