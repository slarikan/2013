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

def setup():
    autotools.autoreconf("-fi")
    # Enable hid2hci in next releases as udev dropped that again
    autotools.configure("--enable-network \
                         --enable-serial \
                         --enable-input \
                         --enable-audio \
                         --enable-service \
                         --enable-gstreamer \
                         --enable-alsa \
                         --enable-usb \
                         --enable-tools \
                         --enable-bccmd \
                         --enable-dfutool \
                         --enable-cups \
                         --enable-hidd \
                         --enable-dund \
                         --enable-pand \
                         --enable-test \
                         --enable-pcmcia \
                         --disable-systemd \
                         --with-systemdunitdir=/lib/systemd/system \
                         --with-ouifile=/usr/share/misc/oui.txt \
                         --enable-hid2hci \
                         --libexecdir=/lib")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Install conf files
    for i in ["audio", "input", "network", "proximity"]:
        pisitools.insinto("/etc/bluetooth", "profiles/%s/%s.conf" % (i,i))
        
    pisitools.insinto("/etc/bluetooth", "src/bluetooth.conf")
    pisitools.insinto("/etc/bluetooth", "src/main.conf")

    # Simple test tools
    for i in ["test-adapter", "test-discovery", "test-health-sink",
               "test-manager", "test-network", "test-proximity", "test-device",
               "test-health", "test-nap", "test-sap-server", "test-thermometer",
               "monitor-bluetooth", "simple-agent", "simple-endpoint", "simple-player",
              "simple-service", "list-devices"]:
        pisitools.dobin("test/%s" % i)

    # Additional tools
    #pisitools.dosbin("tools/hcisecfilter")
    #pisitools.dosbin("tools/ppporc")

    # Install documents
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
