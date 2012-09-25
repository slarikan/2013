#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.dodir("/opt")
    pisitools.insinto("/opt//eclipse", "plugins")
    pisitools.insinto("/opt/eclipse", "features")
    
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.launching_3.6.100.v20120523-1953.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.apt.ui_3.3.300.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt_3.8.0.v201206081200.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.launching.source_3.6.100.v20120523-1953.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.ant.ui.source_3.5.300.v20120523-1742.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.annotation.source_1.0.0.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.junit.source_3.7.100.v20120523-1543.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.compiler.tool_1.0.101.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.junit4.runtime_1.1.200.v20120523-1257.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.debug.source_3.7.100.v20120529-1702.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.apt.ui.source_3.3.300.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.debug.ui_3.6.100.v20120530-1425.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.annotation_1.0.0.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.junit.core.source_3.7.100.v20120523-1257.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.apt.pluggable.core_1.0.400.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.junit_3.7.100.v20120523-1543.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.ui_3.8.0.v20120524-1551.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.debug.ui.source_3.6.100.v20120530-1425.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.core.manipulation_1.5.0.v20120523-1543.jar")
    pisitools.remove("/opt/eclipse/plugins/org.hamcrest.core.source_1.1.0.v20090501071000.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.ant.launching_1.0.200.v20120530-120908.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.core.source_3.8.1.v20120531-0637.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.apt.core_3.3.500.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.junit.source_3.8.2.v3_8_2_v20100427-1100.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.apt.pluggable.core.source_1.0.400.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.doc.user_3.8.0.v20120606-134218.jar")
    pisitools.remove("/opt/eclipse/plugins/org.hamcrest.core_1.1.0.v20090501071000.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.junit.runtime_3.4.300.v20120523-1257.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.junit.runtime.source_3.4.300.v20120523-1257.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.junit.core_3.7.100.v20120523-1257.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.compiler.apt_1.0.500.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.ant.ui_3.5.300.v20120523-1742.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.source_3.8.0.v201206081200.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.compiler.tool.source_1.0.101.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.compiler.apt.source_1.0.500.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.junit4.runtime.source_1.1.200.v20120523-1257.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.ant.launching.source_1.0.200.v20120530-120908.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.ui.source_3.8.0.v20120524-1551.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.doc.isv_3.8.0.v20120604-121952.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.apt.core.source_3.3.500.v20120522-1651.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.core.manipulation.source_1.5.0.v20120523-1543.jar")
    pisitools.remove("/opt/eclipse/plugins/org.junit.source_4.10.0.v4_10_0_v20120426-0900.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.jdt.core_3.8.1.v20120531-0637.jar")
