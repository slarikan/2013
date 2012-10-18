#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.util import run_batch, check_file_hash, Error

WorkDir = 

def setup():
    pass

def install():
    pisitools.dodir("/opt")
    shelltools.system("./construct unbundle-jdk %s/opt/sun-jdk %s/opt/sun-jre"% (get.installDIR(),get.installDIR()))

    pisitools.dodir("/usr/lib/browser-plugins")

    # Next generation Java plugin is needed by Firefox 3.6+
    # http://java.sun.com/javase/6/webnotes/install/jre/manual-plugin-install-linux.html
    pisitools.dosym("/opt/sun-jre/lib/%s/libnpjp2.so" % Arch.replace("i586", "i386"), "/usr/lib/browser-plugins/javaplugin.so")

    for doc in ["COPYRIGHT", "LICENSE", "README.html", "THIRDPARTYLICENSEREADME.txt",
                "register.html", "register_ja.html", "register_zh_CN.html"]:
        file = "%s/opt/sun-jdk/%s" % (get.installDIR(), doc)
        pisitools.dodoc(file)
        shelltools.unlink(file)
