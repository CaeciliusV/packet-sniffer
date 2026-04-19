# Packet Sniffer

## Status: Complete

This is a software surveillance tool that is able to scan through the packets coming to and from the device and then separates the packets with an IP layer and packets without. It then time stamps when each packet is passed and then uploads the packets with an IP layer to a txt file. I built this to have a better understanding of networks and packets.

This project is part of a bigger series in which I learn real-world cybersecurity skills alongside my T Level

## What it does

- Scans the network
- Ignores any packets without IP layers
- Adds the packets with IP layers to a list and time stamps them
- After 100 scans adds the packets with IP layers to a txt file
- Works in the background

## What I learned

- What packets are
- The different protocols (Specifically TCP, ICMP and UDP)
- When and why TCP would be used over UDP and vice-versa
- How to scan the traffic of my device
- What Source and Destination are

## How to run it

1. Download or clone this repository
2. Have scapy installed
3. Run the packet sniffer
4. Wait a couple of seconds
5. Open the file named: packet_logs.txt

## Example output

Upload Date & Time: 2026-04-19 18:21:16.163463
Timestamp: 2026-04-19 18:21:07.782479 | Source: 0.0.0.0 --> Destination: 255.255.255.255 | Protocol: UDP
Timestamp: 2026-04-19 18:21:08.161376 | Source: 111.111.1.111 --> Destination: 255.255.255.255 | Protocol: UDP
Timestamp: 2026-04-19 18:21:09.145737 | Source: 111.111.1.111 --> Destination: 555.55.555.55 | Protocol: TCP
Timestamp: 2026-04-19 18:21:09.234781 | Source: 222.22.222.2 --> Destination: 667.66.6.66 | Protocol: TCP
Timestamp: 2026-04-19 18:21:11.194206 | Source: 333.333.3.33 --> Destination: 255.255.255.255 | Protocol: UDP
Timestamp: 2026-04-19 18:21:11.112582 | Source: 444.444.4.444 --> Destination: 255.255.255.255 | Protocol: UDP

## Limitations

- Doesnt tell you what information is being passed in encrypted traffic e.g. HTTPS
- Mainly tells you your own traffic
- Only captures packets with an IP layer
- Doesnt capture traffic on other networks or interfaces
- Only identifies three protocols by name: TCP, UDP and ICMP anything else will show Unknown followed by its protocol number 

## Tools used

- Python 3
- scapy
- packet_logs.txt

## Ethical Note
This tool was made for educational purposes only
Under the Computer Misuse act 1990 using this tool on any machine without permission/authorisation is illegal







