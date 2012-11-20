#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt
import shutil
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

#shelltools.export("USER","q")
WorkDir="sendmail-8.14.5"

def setup():
    pass
  
def build():
    shelltools.system('./Build')

def install():
    pisitools.dodir("/usr/sbin")
    pisitools.dodir("/usr/share/man/man8")
    pisitools.dodir("/usr/share/man/man5")
    pisitools.dodir("/usr/share/man/man1")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #shelltools.system()
 
