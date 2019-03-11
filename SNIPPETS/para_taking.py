
from scapy.all import * 
def sniffPackets(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        pckt_src=packet[IP].src
        pckt_dst=packet[IP].dst
        pckt_ttl=packet[IP].ttl
        pckt_len=packet[IP].len
        pckt_win=packet[TCP].window
        
        print(pckt_src,',',pckt_dst,',',pckt_ttl,',',pckt_win,',',pckt_len)

def main():
    print("custom packet sniffer")
    sniff(iface=conf.iface,prn=sniffPackets)   
          
          
if __name__ == '__main__':
          main()

