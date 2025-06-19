# sniffer.py
from scapy.all import sniff, IP
from logger import insert_packet, create_db
from datetime import datetime

create_db()

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        length = len(packet)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_packet(src_ip, dst_ip, str(proto), length, timestamp)
        print(f"[LOG] {src_ip} → {dst_ip} | Protocol: {proto} | Len: {length}")

print("[*] Starting packet capture... Press CTRL+C to stop.")
sniff(prn=process_packet, store=0)
