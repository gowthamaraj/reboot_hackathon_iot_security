
# EDA Packages
import pandas as pd
import numpy as np
import random
from scapy.all import *
import psutil

# Machine Learning Packages
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.metrics import classification_report, confusion_matrix  

dataset = pd.read_csv("data_set.csv")


X = dataset.iloc[:, 2:5].values  
y = dataset.iloc[:, 5].values 

from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)

client.create_database('network')
client.switch_database('network')

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X,y)

#Predict Output
def sniffPackets(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        pckt_src=packet[IP].src
        pckt_dst=packet[IP].dst
        pckt_ttl=packet[IP].ttl
        pckt_len=packet[IP].len
        pckt_win=packet[TCP].window
        
        #print(pckt_src,',',pckt_dst,',',pckt_ttl,',',pckt_win,',',pckt_len)

        predicted= model.predict([[pckt_ttl,pckt_win,pckt_len]])
        pre=int(predicted)
        json_body = [
        {
        "measurement": "monitor",
        "tags": {
            "user": "impact",
        },
        "fields": {
            "source": pckt_src,
            "destination": pckt_dst,
            "ttl": pckt_ttl,
            "len": pckt_len,
            "win": pckt_win,
            "prediction": pre
            
        }
        }
        ]
        client.write_points(json_body)


def main():
    print("custom packet sniffer")
    sniff(iface=conf.iface,prn=sniffPackets)   
          
          
if __name__ == '__main__':
          main()
