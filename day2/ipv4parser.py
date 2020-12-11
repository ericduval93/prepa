#!/usr/bin/python3

import ipaddress

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

def Dec2Bit( num ):
    return int(bin(num).replace("0b", ""))

def ipv4_parser(ip_addr, ip_mask):
    addr = [0, 0, 0, 0]
    mask = [0, 0, 0, 0]

    addr = [int(x) for x in ip_addr.split(".")]
    mask = [int(x) for x in ip_mask.split(".")]

    network = [addr[i] & mask[i] for i in range(4)]
    cidr = sum((bin(x).count('1') for x in mask))
    bcas = [(addr[i] & mask[i]) | (255^mask[i]) for i in range(4)]
    host_id = [abs(network[i] - addr[i]) for i in range(4)]

    return network, cidr, bcas, host_id

if __name__ == '__main__':

    mynet, cidr, bcas, host_id = ipv4_parser( '192.168.50.1', '255.255.255.0' )
    print("network = {}/{} - netmask = {} - hostid = {}".format('.'.join(map(str,mynet)),cidr,'.'.join(map(str,bcas)),'.'.join(map(str,host_id))))

    mynet, cidr, bcas, host_id = ipv4_parser( '192.168.50.129', '255.255.255.192' )
    print("network = {}/{} - netmask = {} - hostid = {}".format('.'.join(map(str,mynet)),cidr,'.'.join(map(str,bcas)),'.'.join(map(str,host_id))))

    mynet, cidr, bcas, host_id = ipv4_parser( '65.196.188.53', '255.255.240.0' )
    print("network = {}/{} - netmask = {} - hostid = {}".format('.'.join(map(str,mynet)),cidr,'.'.join(map(str,bcas)),'.'.join(map(str,host_id))))

exit( 0 )

# test.assert_equals(
#     ipv4__parser('192.168.50.1', '255.255.255.0'),
#     ('192.168.50.0', '0.0.0.1')
# )
# test.assert_equals(
#     ipv4__parser('192.168.50.129', '255.255.255.192'),
#     ('192.168.50.128', '0.0.0.1')
# )
# test.assert_equals(
#     ipv4__parser('65.196.188.53', '255.255.240.0'),
#     ('65.196.176.0', '0.0.12.53')
# )
