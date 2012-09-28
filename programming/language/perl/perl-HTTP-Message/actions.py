#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.remove("/usr/share/man/man3/HTTP::Request::Common.3pm")
    pisitools.remove("/usr/share/man/man3/HTTP::Request.3pm")
    pisitools.remove("/usr/share/man/man3/HTTP::Status.3pm")
    pisitools.remove("/usr/share/man/man3/HTTP::Config.3pm")
    pisitools.remove("/usr/share/man/man3/HTTP::Headers::Util.3pm")
    pisitools.remove("/usr/share/man/man3/HTTP::Response.3pm")
    pisitools.remove("/usr/share/man/man3/HTTP::Headers.3pm")
    pisitools.remove("/usr/share/man/man3/HTTP::Message.3pm")