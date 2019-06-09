#!/usr/bin/python
from scapy.all import *
import sys
import time
from struct import pack, unpack

#x = IP(ttl=64)
#x.src="20.0.0.2"
#x.dst="20.0.0.6"
#send(x, count=2000)

#for i in range(5):
 # p1=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.1',version=4,ttl=64)
  #p2=GRE()
  #p3=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.3',version=4,ttl=64)
  #p4=GRE()
  #p5=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.2',version=4,ttl=64)
  #p6=UDP(dport=40000, sport=40000)
  #p7=pack('dQ',time.time(),i)
  #packet=p1/p2/p3/p4/p5/p6/p7
  #send(packet)
  #packet

s = conf.L3socket(iface="eth1")
packetSentCount = 1

# Dev1 R1 R2 R5 R3 R1 Dev1
for i in range(1):
  p1=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.1',version=4,ttl=64)
  p2=GRE()
  p3=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.1',version=4,ttl=64)
  p4=GRE()
  p5=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.7',version=4,ttl=64)
  p6=GRE()
  p7=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.10',version=4,ttl=64)
  p8=GRE()
  p9=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.2',version=4,ttl=64)
  p10=GRE()
  p11=IP(src='20.0.0.2',proto=17,tos=0,dst='20.0.0.2',version=4,ttl=64)
  p12=UDP(dport=40000, sport=40000)
  p13=pack('dlll',time.time(),i,0,packetSentCount)
  packet=p1/p2/p3/p4/p5/p6/p7/p8/p9/p10/p11/p12/p13
  s.send(packet)
  packet

# Dev1 R1 R2 R4 R3 R1 Dev1
for j in range(1):
  p1=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.1',version=4,ttl=64)
  p2=GRE()
  p3=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.1',version=4,ttl=64)
  p4=GRE()
  p5=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.5',version=4,ttl=64)
  p6=GRE()
  p7=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.10',version=4,ttl=64)
  p8=GRE()
  p9=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.2',version=4,ttl=64)
  p10=GRE()
  p11=IP(src='20.0.0.2',proto=17,tos=0,dst='20.0.0.2',version=4,ttl=64)
  p12=UDP(dport=40000, sport=40000)
  p13=pack('dlll',time.time(),i,1,packetSentCount)
  packet=p1/p2/p3/p4/p5/p6/p7/p8/p9/p10/p11/p12/p13
  s.send(packet)
  packet  

# Dev1 R1 R3 R5 R2 R1 Dev1
for i in range(1):
  p1=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.1',version=4,ttl=64)
  p2=GRE()
  p3=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.3',version=4,ttl=64)
  p4=GRE()
  p5=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.9',version=4,ttl=64)
  p6=GRE()
  p7=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.6',version=4,ttl=64)
  p8=GRE()
  p9=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.0',version=4,ttl=64)
  p10=GRE()
  p11=IP(src='20.0.0.2',proto=17,tos=0,dst='20.0.0.2',version=4,ttl=64)
  p12=UDP(dport=40000, sport=40000)
  p13=pack('dlll',time.time(),i,2,packetSentCount)
  packet=p1/p2/p3/p4/p5/p6/p7/p8/p9/p10/p11/p12/p13
  s.send(packet)
  packet
 

# Dev1 R1 R3 R4 R2 R1 Dev1
for i in range(1):
  p1=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.1',version=4,ttl=64)
  p2=GRE()
  p3=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.3',version=4,ttl=64)
  p4=GRE()
  p5=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.11',version=4,ttl=64)
  p6=GRE()
  p7=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.4',version=4,ttl=64)
  p8=GRE()
  p9=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.0',version=4,ttl=64)
  p10=GRE()
  p11=IP(src='20.0.0.2',proto=17,tos=0,dst='20.0.0.2',version=4,ttl=64)
  p12=UDP(dport=40000, sport=40000)
  p13=pack('dlll',time.time(),i,3,packetSentCount)
  packet=p1/p2/p3/p4/p5/p6/p7/p8/p9/p10/p11/p12/p13
  s.send(packet)
  packet

# Dev1 R1 R2 R4 R6 R5 R3  R1 Dev1
for i in range(1):
  p1=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.1',version=4,ttl=64)
  p2=GRE()
  p3=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.1',version=4,ttl=64)
  p4=GRE()
  p5=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.5',version=4,ttl=64)
  p6=GRE()
  p7=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.13',version=4,ttl=64)
  p8=GRE()
  p9=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.14',version=4,ttl=64)
  p10=GRE()
  p11=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.8',version=4,ttl=64)
  p12=GRE()
  p13=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.2',version=4,ttl=64)
  p14=GRE()
  p15=IP(src='20.0.0.2',proto=17,tos=0,dst='20.0.0.2',version=4,ttl=64)
  p16=UDP(dport=40000, sport=40000)
  p17=pack('dlll',time.time(),i,4,packetSentCount)
  packet=p1/p2/p3/p4/p5/p6/p7/p8/p9/p10/p11/p12/p13/p14/p15/p16/p17
  s.send(packet)
  packet

# Dev1 R1 R3 R5 R6 R4 R2 R1 Dev1
for i in range(1):
  p1=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.1',version=4,ttl=64)
  p2=GRE()
  p3=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.3',version=4,ttl=64)
  p4=GRE()
  p5=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.9',version=4,ttl=64)
  p6=GRE()
  p7=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.15',version=4,ttl=64)
  p8=GRE()
  p9=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.12',version=4,ttl=64)
  p10=GRE()
  p11=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.4',version=4,ttl=64)
  p12=GRE()
  p13=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.0',version=4,ttl=64)
  p14=GRE()
  p15=IP(src='20.0.0.2',proto=17,tos=0,dst='20.0.0.2',version=4,ttl=64)
  p16=UDP(dport=40000, sport=40000)
  p17=pack('dlll',time.time(),i,5,packetSentCount)
  packet=p1/p2/p3/p4/p5/p6/p7/p8/p9/p10/p11/p12/p13/p14/p15/p16/p17
  s.send(packet)
  packet

# Dev1 R1 R2 R5 R6 R4 R3 R1 Dev1
for i in range(1):
  p1=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.1',version=4,ttl=64)
  p2=GRE()
  p3=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.1',version=4,ttl=64)
  p4=GRE()
  p5=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.7',version=4,ttl=64)
  p6=GRE()
  p7=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.15',version=4,ttl=64)
  p8=GRE()
  p9=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.12',version=4,ttl=64)
  p10=GRE()
  p11=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.10',version=4,ttl=64)
  p12=GRE()
  p13=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.2',version=4,ttl=64)
  p14=GRE()
  p15=IP(src='20.0.0.2',proto=17,tos=0,dst='20.0.0.2',version=4,ttl=64)
  p16=UDP(dport=40000, sport=40000)
  p17=pack('dlll',time.time(),i,6,packetSentCount)
  packet=p1/p2/p3/p4/p5/p6/p7/p8/p9/p10/p11/p12/p13/p14/p15/p16/p17
  s.send(packet)
  packet

# Dev1 R1 R3 R4 R6 R5 R2 R1 Dev1
for i in range(1):
  p1=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.1',version=4,ttl=64)
  p2=GRE()
  p3=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.3',version=4,ttl=64)
  p4=GRE()
  p5=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.11',version=4,ttl=64)
  p6=GRE()
  p7=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.13',version=4,ttl=64)
  p8=GRE()
  p9=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.14',version=4,ttl=64)
  p10=GRE()
  p11=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.6',version=4,ttl=64)
  p12=GRE()
  p13=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.0',version=4,ttl=64)
  p14=GRE()
  p15=IP(src='20.0.0.2',proto=17,tos=0,dst='20.0.0.2',version=4,ttl=64)
  p16=UDP(dport=40000, sport=40000)
  p17=pack('dlll',time.time(),i,7,packetSentCount)
  packet=p1/p2/p3/p4/p5/p6/p7/p8/p9/p10/p11/p12/p13/p14/p15/p16/p17
  s.send(packet)
  packet
  
# Dev1 R1 R3 R4 R6 R5 R3 R1 Dev1
for i in range(1):
  p1=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.1',version=4,ttl=64)
  p2=GRE()
  p3=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.3',version=4,ttl=64)
  p4=GRE()
  p5=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.11',version=4,ttl=64)
  p6=GRE()
  p7=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.13',version=4,ttl=64)
  p8=GRE()
  p9=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.14',version=4,ttl=64)
  p10=GRE()
  p11=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.8',version=4,ttl=64)
  p12=GRE()
  p13=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.2',version=4,ttl=64)
  p14=GRE()
  p15=IP(src='20.0.0.2',proto=17,tos=0,dst='20.0.0.2',version=4,ttl=64)
  p16=UDP(dport=40000, sport=40000)
  p17=pack('dlll',time.time(),i,8,packetSentCount)
  packet=p1/p2/p3/p4/p5/p6/p7/p8/p9/p10/p11/p12/p13/p14/p15/p16/p17
  s.send(packet)
  packet

# Dev1 R1 R2 R5 R6 R4 R2 R1 Dev1
for i in range(1):
  p1=IP(src='20.0.0.2',proto=47,tos=0,dst='20.0.0.1',version=4,ttl=64)
  p2=GRE()
  p3=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.1',version=4,ttl=64)
  p4=GRE()
  p5=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.7',version=4,ttl=64)
  p6=GRE()
  p7=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.15',version=4,ttl=64)
  p8=GRE()
  p9=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.12',version=4,ttl=64)
  p10=GRE()
  p11=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.4',version=4,ttl=64)
  p12=GRE()
  p13=IP(src='20.0.0.2',proto=47,tos=0,dst='10.1.1.0',version=4,ttl=64)
  p14=GRE()
  p15=IP(src='20.0.0.2',proto=17,tos=0,dst='20.0.0.2',version=4,ttl=64)
  p16=UDP(dport=40000, sport=40000)
  p17=pack('dlll',time.time(),i,9,packetSentCount)
  packet=p1/p2/p3/p4/p5/p6/p7/p8/p9/p10/p11/p12/p13/p14/p15/p16/p17
  s.send(packet)
  packet

