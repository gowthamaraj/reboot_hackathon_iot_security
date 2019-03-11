from scapy.all import * 
def sniffPackets(packet):
    if packet.haslayer(IP):
        pckt_src=packet[IP].src
        pckt_dst=packet[IP].dst
        pckt_ttl=packet[IP].ttl
        print('IP Packet: ',pckt_src,' is going to ',pckt_dst,' and has ttl value ',pckt_ttl)

def main():
    print("custom packet sniffer")
    sniff(filter="ip",iface=conf.iface,prn=sniffPackets)   
          
          
if __name__ == '__main__':
          main()