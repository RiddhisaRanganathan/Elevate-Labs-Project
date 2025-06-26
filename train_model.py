# Final train_model.py 

# train_model.py
import sqlite3
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import pickle

# List of features you want to use
FEATURES = ['src_port', 'dst_port', 'length', 'ttl', 'window_size']

# Load data
conn = sqlite3.connect("packets.db")
df = pd.read_sql_query("SELECT * FROM packet_logs", conn)
conn.close()

# Remove rows with NULLs in important fields
df = df.dropna(subset=FEATURES)

X = df[FEATURES]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Isolation Forest
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X_scaled)

# Save model and scaler to ml/
with open("ml/anomaly_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("ml/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("[✔] Model trained on full feature set from packets.db and saved.")
