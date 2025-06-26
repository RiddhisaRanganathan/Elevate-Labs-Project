# Final anomaly_detector.py 

# anomaly_detector.py
import sqlite3
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Features to fetch and use
FEATURES = ['src_port', 'dst_port', 'length', 'ttl', 'window_size']

def fetch_latest_packets(limit=100):
    conn = sqlite3.connect("packets.db")
    c = conn.cursor()
    c.execute(f"""
        SELECT {', '.join(FEATURES)} FROM packet_logs
        ORDER BY id DESC LIMIT ?
    """, (limit,))
    rows = c.fetchall()
    conn.close()
    return rows

def detect_anomalies(limit=100, return_results=False):
    # Correct path to pkl files
    with open("ml/anomaly_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("ml/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    rows = fetch_latest_packets(limit)
    if not rows:
        print("No packets to analyze.")
        return []

    df = pd.DataFrame(rows, columns=FEATURES)
    scaled = scaler.transform(df)
    predictions = model.predict(scaled)

    labels = ['Normal' if p == 1 else 'Anomaly' for p in predictions]

    print("\n=== Anomaly Detection Results ===")
    for i, label in enumerate(labels):
        print(f"Packet {i+1}: {label}")

    if return_results:
        return labels

if __name__ == "__main__":
    detect_anomalies()
