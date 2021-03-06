import logging
import lxc

from ipaddress import IPv4Address


# returns the next available IP address
def _next_ip():
    ips = []

    for name in lxc.list_containers():
        container = lxc.Container(name)
        # get the ip as set in the config
        ip = container.get_config_item('lxc.net.0.ipv4.address')

        if ip:
            ips.append(IPv4Address(ip.split('/')[0]))

    if not ips:
        # return a default first address
        return IPv4Address('10.0.3.2')

    # returns the ip address just after the max current address
    return max(ips) + 1


# create a new container
def create(name, distro, release, arch):
    container = lxc.Container(name)

    # check if the container already exists
    if container.defined:
        logging.error('A container with the name "{name}" is already defined')
        return False

    # find the next available IP address
    ip = _next_ip()

    # create the container
    container.create('download', 0, {
        'dist': distro,
        'release': release,
        'arch': arch,
    })

    # set the container's ip address
    container.append_config_item('lxc.net.0.ipv4.address', str(ip))
    container.save_config()

    return True
