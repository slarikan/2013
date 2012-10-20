#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import libtools

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.echo("docs/gtk-doc.make", "EXTRA_DIST=")
    autotools.autoreconf("-fi")
    libtools.libtoolize("--force")
    options = " ac_cv_header_sys_capability_h=yes \
                --bindir=/bin \
                --sbindir=/sbin \
                --docdir=/usr/share/doc/udev \
                --libdir=/usr/lib \
                --libexecdir=/lib/udev \
                --with-distro=other \
                --with-firmware-path=/lib/firmware/updates:/lib/firmware \
                --with-html-dir=/usr/share/doc/udev/html \
                --with-rootlibdir=/lib \
                --with-rootprefix= \
                --disable-coredump \
                --disable-hostnamed \
                --disable-ima \
                --disable-libcryptsetup \
                --disable-localed \
                --disable-logind \
                --disable-nls \
                --disable-quotacheck \
                --disable-readahead \
                --enable-split-usr \
                --disable-timedated \
                --disable-xz \
                --enable-gudev \
                --disable-selinux \
                --disable-static \
                --disable-introspection"

    autotools.configure(options)

def build():
    shelltools.echo("Makefile.extra", "BUILT_SOURCES: $(BUILT_SOURCES)")
    autotools.make("-f Makefile -f Makefile.extra")

    targets = " udevd \
                udevadm \
                libudev.la \
                ata_id \
                cdrom_id \
                collect \
                scsi_id \
                v4l_id \
                accelerometer \
                mtd_probe \
                man/udev.7 \
                man/udevadm.8 \
                man/udevd.8 \
                keymap \
                libgudev-1.0.la"
    autotools.make(targets)

    autotools.make("-C docs/libudev")
    autotools.make("-C docs/gudev")

#~ def check():
    #~ autotools.make("check")
#~ 
def install():
    targets ="  install-libLTLIBRARIES \
                install-includeHEADERS \
                install-libgudev_includeHEADERS \
                install-sbinPROGRAMS \
                install-binPROGRAMS \
                install-rootlibexecPROGRAMS \
                install-udevlibexecPROGRAMS \
                install-dist_systemunitDATA \
                install-dist_udevconfDATA \
                install-dist_udevhomeSCRIPTS \
                install-dist_udevkeymapDATA \
                install-dist_udevkeymapforcerelDATA \
                install-dist_udevrulesDATA \
                install-girDATA \
                install-man7 \
                install-man8 \
                install-nodist_systemunitDATA \
                install-pkgconfiglibDATA \
                install-sharepkgconfigDATA \
                install-typelibsDATA \
                install-dist_docDATA \
                udev-confdirs \
                systemd-install-hook \
                rootlibexec_PROGRAMS='' \
                bin_PROGRAMS='' \
                sbin_PROGRAMS='udevd udevadm' \
                lib_LTLIBRARIES='libudev.la libgudev-1.0.la' \
                MANPAGES='man/udev.7 man/udevadm.8 man/udevd.8' \
                MANPAGES_ALIAS='man/systemd-udevd.8' \
                pkgconfiglib_DATA='src/libudev/libudev.pc src/gudev/gudev-1.0.pc' \
                dist_systemunit_DATA='units/systemd-udevd-control.socket \
                                      units/systemd-udevd-kernel.socket' \
                nodist_systemunit_DATA='units/systemd-udevd.service \
                                        units/systemd-udev-trigger.service \
                                        units/systemd-udev-settle.service'"

    autotools.make("DESTDIR=%s %s" % (get.installDIR(),targets))

    # Create needed directories
    #for d in ("", "net", "pts", "shm", "hugepages"):
         #pisitools.dodir("/lib/udev/devices/%s" % d)
         
    #Create vol_id and scsi_id symlinks in /sbin probably needed by multipath-tools
    pisitools.dosym("/lib/udev/scsi_id", "/sbin/scsi_id")
    
    #Create /etc/udev/rules.d for backward compatibility
    pisitools.dodir("/etc/udev/rules.d")
    pisitools.dodoc("README", "TODO")
