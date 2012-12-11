#/usr/bin/python

from pisi.util import run_batch

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not run_batch("cat /etc/passwd | grep polkitd")[1].split(":")[5] == "/var/lib/polkit-1":
        run_batch("usermod -d /var/lib/polkit-1 polkitd")
