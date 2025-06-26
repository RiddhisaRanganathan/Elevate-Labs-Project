# Elevate-Labs-Project

lightweight_ids_project/
│
├── dataset/
│   ├── KDDTrain.txt          # NSL-KDD training dataset
│   └── KDDTest.txt           # NSL-KDD testing dataset
│
├── ml/
│   ├── anomaly_detector.py  # Real-time anomaly detection logic
│   ├── anomaly_model.pkl    # Trained Isolation Forest model
│   ├── scaler.pkl           # Scaler used for normalizing features
│   └── train_model.py       # Trains model using packets.db or KDD dataset
│
├── sniff/
│   ├── __init__.py
│   ├── logger.py            # Creates and writes to packets.db
│   ├── result.py            # Displays stored packets
│   └── sniffer.py           # Captures live packets with Scapy
│
└── packets.db               # SQLite database storing captured packets
