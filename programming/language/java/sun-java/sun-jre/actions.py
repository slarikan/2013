#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
import shutil
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
WorkDir="jre1.7.0_09"
def setup():
    pass

def install():
    pisitools.dodir("/opt")
#   shelltools.copy("/var/pisi/sun-jre-1.7.0_09-1/work/jre1.7.0_09","/var/pisi/sun-jre-1.7.0_09-1/install/opt/sun-jdk/jre")
    
    shutil.copytree("/var/pisi/sun-jre-1.7.0_09-1/work/jre1.7.0_09","/var/pisi/sun-jre-1.7.0_09-1/install/opt/sun-jdk/jre") # alternative for upper line and it work
   
    pisitools.dodir("/usr/lib/browser-plugins")
    pisitools.dosym("/opt/sun-jdk/jre/lib/amd64/libnpjp2.so" , "/usr/lib/browser-plugins/javaplugin.so")
    
    shutil.rmtree("/var/pisi/sun-jre-1.7.0_09-1/install/opt/sun-jdk/jre/plugin/desktop/") 
   
    pisitools.dosym("/opt/sun-jdk/jre" , "/opt/sun-jre")