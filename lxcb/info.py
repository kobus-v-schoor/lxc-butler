import os
import getpass

# the user's username
username = getpass.getuser()

# try and figure out the distro name and release
# TODO add methods for other distros
distro = None
release = None
arch = 'amd64'

if os.path.isfile('/etc/os-release'):
    with open('/etc/os-release', 'r') as f:
        for line in f.readlines():
            key, value = line.strip().split('=', maxsplit=1)
            if key == 'ID':
                distro = value.strip('"')
            elif key == 'VERSION_CODENAME':
                release = value.strip('"')
