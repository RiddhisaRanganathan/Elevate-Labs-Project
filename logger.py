# logger.py
import sqlite3

def create_db():
    conn = sqlite3.connect("packets.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS packet_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            src_ip TEXT,
            dst_ip TEXT,
            protocol TEXT,
            length INTEGER,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_packet(src_ip, dst_ip, proto, length, timestamp):
    conn = sqlite3.connect("packets.db")
    c = conn.cursor()
    c.execute("INSERT INTO packet_logs (src_ip, dst_ip, protocol, length, timestamp) VALUES (?, ?, ?, ?, ?)",
              (src_ip, dst_ip, proto, length, timestamp))
    conn.commit()
    conn.close()

create_db()