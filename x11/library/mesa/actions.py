# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Mesa-%s" % get.srcVERSION().replace("_", "-")

if get.buildTYPE() == "emul32":
    Libdir = "/usr/lib32"
else:
    Libdir = "/usr/lib"

def setup():
    shelltools.export("CFLAGS", "%s -DNDEBUG" % get.CFLAGS())

    # Fix sandbox violations
    pisitools.dosed("src/gallium/auxiliary/Makefile", "(\$\(PYTHON2\))", r"\1 -B")
    pisitools.dosed("src/gallium/drivers/llvmpipe/Makefile", "(\$\(PYTHON_FLAGS\))", r"\1 -B")

    autotools.autoreconf("-vif")

    # gallium-lvm is enabled by default by commit a86fc719d6402eb482657707741890e69e81700f
    options ="--enable-pic \
              --enable-glx-tls \
              --disable-egl \
              --enable-gallium \
              --with-gallium-drivers=r300,r600,nouveau,swrast \
              --with-driver=dri \
              --with-dri-driverdir=/usr/lib/xorg/modules/dri \
              --with-dri-drivers=i915,i965,nouveau,r200,radeon,swrast"


    if get.buildTYPE() == "emul32":
        # compile with llvm doesn't work for now, test it later
        options += " --libdir=/usr/lib32 \
                     --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
                     --disable-gallium-llvm \
                     --with-gallium-drivers=r600,nouveau,swrast \
                     --enable-32-bit"

        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())

    autotools.configure(options)

    #pisitools.dosed("configs/autoconf", "(PYTHON_FLAGS) = .*", r"\1 = -t")

def build():
#    autotools.make("-C src/glsl glsl_lexer.cpp")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # needed to build xapian-core
    pisitools.dosym("libGL.so.1.2.0", "%s/libGL.so.1.2" % Libdir)

    if get.buildTYPE() == "emul32":
        return

    pisitools.dodoc("docs/COPYING")
    pisitools.dohtml("docs/*")
