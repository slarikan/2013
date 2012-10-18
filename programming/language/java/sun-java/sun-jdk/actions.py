#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import shutil
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="jdk1.7.0_07"

def setup():
    pass

def install():
   # pisitools.dodir("/opt")
    #   shelltools.copy("/var/pisi/sun-jre-1.7.0_09-1/work/jre1.7.0_09","/var/pisi/sun-jre-1.7.0_09-1/install/opt/sun-jdk")
    
    shutil.copytree("/var/pisi/sun-jdk-1.7.0_07-1/work/jdk1.7.0_07","/var/pisi/sun-jdk-1.7.0_07-1/install/opt/sun-jdk") # alternative for upper line and it work   
    shutil.rmtree("/var/pisi/sun-jdk-1.7.0_07-1/install/opt/sun-jdk/jre")  
   