from scapy.all import sniff, IP
import datetime

protocols = {6 : "TCP", 17 : "UDP", 1 : "ICMP"}
packets = []


def prn(packet):
    if IP in packet:
        datetimestr = str(datetime.datetime.now())
        source = packet[IP].src
        destination = packet[IP].dst
        protocol = packet[IP].proto
        protocol = protocols.get(protocol,f"Unknown({protocol})")
        print(f"Timestamp: {datetimestr} | Source: {source} --> Destination: {destination} | Protocol: {protocol}")
        packets.append(f"Timestamp: {datetimestr} | Source: {source} --> Destination: {destination} | Protocol: {protocol}")    


def packet_chunks():
    
    with open("packet_logs.txt", "a") as f:
        datetimestr = str(datetime.datetime.now())
        f.write(f"Upload Date & Time: {datetimestr}")
        f.write("\n")
        for item in packets:
            f.write(item)
            f.write("\n")
        f.write("\n")
    


sniff(prn=prn, count=100)
packet_chunks()
