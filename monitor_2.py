from scapy.all import sniff,ARP
 
pkts = sniff(filter="arp", count=10)
print(pkts.summary())

def arp_display(pkt):
    if pkt[ARP].op == 1:  # who-has (request)
        return f"Request: {pkt[ARP].psrc} is asking about {pkt[ARP].pdst}"
    if pkt[ARP].op == 2:  # is-at (response)
        return f"*Response: {pkt[ARP].hwsrc} has address {pkt[ARP].psrc}"
 
sniff(prn=arp_display, filter="arp", store=0, count=10)