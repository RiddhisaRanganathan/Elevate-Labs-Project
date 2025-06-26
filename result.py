# Final version of result.py

import sqlite3

conn = sqlite3.connect("packets.db")
c = conn.cursor()

# Count total packets saved to the DB
c.execute("SELECT COUNT(*) FROM packet_logs")
total = c.fetchone()[0]
print(f"\nTotal packets saved: {total}\n")

# Show latest 10 packets
print("Showing latest 10 packets:")
for row in c.execute("SELECT * FROM packet_logs ORDER BY id DESC LIMIT 10"):
    print(row)
    
conn.close()
