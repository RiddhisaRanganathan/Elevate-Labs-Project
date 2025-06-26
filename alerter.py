# alerter.py

from ml.anomaly_detector import detect_anomalies

THRESHOLD = 10  # You can adjust this based on network noise level

def monitor():
    print("[*] Monitoring for abnormal traffic...\n")
    results = detect_anomalies(limit=100, return_results=True)
    
    anomaly_count = results.count("Anomaly")
    print(f"\nAnomalies in last 100 packets: {anomaly_count}")

    if anomaly_count > THRESHOLD:
        print("🚨 ALERT: Too many anomalies detected!")
        # Optional: trigger email, write to file, show GUI popup etc.
    else:
        print("✅ Network status: Normal")

if __name__ == "__main__":
    monitor()
