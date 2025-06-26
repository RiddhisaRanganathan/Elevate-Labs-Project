# Final version of logger.py

import sqlite3

# Creates a SQLite database file packets.db with a table called packet_logs
def create_db():
    conn = sqlite3.connect("packets.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS packet_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            src_ip TEXT,
            dst_ip TEXT,
            src_port INTEGER,
            dst_port INTEGER,
            protocol TEXT,
            length INTEGER,
            flags TEXT,
            ttl INTEGER,
            window_size INTEGER,
            timestamp REAL
        )
    """)
    conn.commit()
    conn.close()

# Inserts one packet’s information into the packet_logs table with all required fields.
def insert_packet(src_ip, dst_ip, src_port, dst_port, proto, length, flags, ttl, window_size, timestamp):
    conn = sqlite3.connect("packets.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO packet_logs (
            src_ip, dst_ip, src_port, dst_port, protocol,
            length, flags, ttl, window_size, timestamp
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (src_ip, dst_ip, src_port, dst_port, proto, length, flags, ttl, window_size, timestamp))
    conn.commit()
    conn.close()

create_db()
