# Elevate-Labs-Project

# Lightweight Intrusion Detection System (IDS) with ML-Based Anomaly Detection

This project is a lightweight Intrusion Detection System (IDS) built using Python, Scapy, SQLite, and a machine learning model for anomaly detection. It captures network packets, extracts meaningful features, and flags suspicious traffic based on trained behavior.

## Background
I first tested my project using the NSL-KDD dataset to make sure the machine learning model and code were working correctly. After that, I used my own captured network packets to retrain the model. Now the system works fully on real packet data collected from my network, and it can detect anomalies based on that.

---

## Features Implemented

### Packet Sniffing
- Captures network traffic using `scapy`
- Extracts features like:
  - Source/Destination IP and Port
  - Protocol
  - Packet length
  - TTL
  - TCP flags
  - Window size
  - Timestamp

### Packet Logging to Database
- Stores extracted packet data in `packets.db` using `sqlite3`
- Table schema designed to support ML-based analysis

### Machine Learning-Based Detection
- Preprocessed captured packets and trained a model using `scikit-learn`
- Used features: `src_port`, `dst_port`, `length`, `ttl`, `window_size`
- Saves trained model and scaler as `anomaly_model.pkl` and `scaler.pkl`

### Anomaly Detection
- Analyzes recent packets stored in database
- Predicts and labels packets as:
  - `Normal`
  - `Anomaly`
- Displays detection results in console

### Alerting System
- Checks the latest packets for anomalies
- Triggers console alerts if anomaly count exceeds a threshold

###  How to Run
- 1. Start by running sniffer.py to capture and log live network packets into the packets.db SQLite database.
- 2. After collecting a sufficient number of packets, run train_model.py to train a machine learning model and generate the scaler and classifier files.
- 3. Once the model is trained, run anomaly_detector.py to analyze the latest captured packets and classify them as normal or anomalous.
- 4. To continuously monitor packet logs and raise alerts if too many anomalies are found, run alerter.py. It internally schedules periodic checks without needing a separate scheduler setup.
 
### Output:

Results have been added both as screenshot and as text in this repository itself.
