#!/usr/bin/env python

from scapy.all import *

if __name__ == "__main__":
    # Packet config
    src_ip = '192.168.56.102'
    dst_ip = '192.168.56.101'
    src_port = 443
    dst_port = 80

    # Construct the packet
    mypac = IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port)

    # View the packet description
    print("Packet (display): ")
    mypac.display()

    print("Packet (summary): ")
    mypac.summary

    # Send the packet
    send(mypac)
