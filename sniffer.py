from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        print(f"[+] {src} -> {dst} | Protocol: {proto}")
        
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"    Payload: {payload[:50]}")

print("[*] Starting sniffer... Press Ctrl+C to stop")
sniff(prn=packet_callback, store=0)
