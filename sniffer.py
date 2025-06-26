# Final version of sniffer.py

# sniffer.py
from scapy.all import sniff, IP, TCP, UDP
import time
from logger import insert_packet

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        length = len(packet)
        timestamp = time.time()

        # Default values
        src_port = dst_port = ttl = flags = window_size = None

        ttl = packet[IP].ttl

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            flags = str(packet[TCP].flags)
            window_size = packet[TCP].window
            protocol = "TCP"
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            protocol = "UDP"
        else:
            protocol = "Other"

        print(f"[PACKET] {src_ip}:{src_port} → {dst_ip}:{dst_port} | Proto: {protocol} | Len: {length} | Flags: {flags} | TTL: {ttl} | Win: {window_size} | Time: {timestamp}")
        insert_packet(src_ip, dst_ip, src_port, dst_port, protocol, length, flags, ttl, window_size, timestamp)

print("[*] Starting packet capture... ")
sniff(prn=process_packet, store=False, filter="ip")
