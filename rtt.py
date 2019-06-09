#!/usr/bin/python
from struct import pack,unpack
from scapy.all import *


def print_return_packet_details(x):
    sendTime,seq,probe,total=unpack('dlll',x.load)
    print ("RTT is %s seconds" % (x.time - sendTime),seq,probe,total)
sniff(iface="eth1",filter="udp and port 40000 and src 20.0.0.2 and dst 20.0.0.2", count=100, prn= print_return_packet_details)

