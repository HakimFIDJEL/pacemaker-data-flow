# producer.py

#!/usr/bin/env python3
import os, json, uuid, time, random, signal, sys
from confluent_kafka import Producer

# Paramètres
INTERVAL = 1.0
ALERT_RATE = 0.02
BATTERY_DECAY = 0.01
TOPIC = os.getenv("KAFKA_TOPIC", "pacemaker")
BOOTSTRAP = os.getenv("BOOTSTRAP_SERVERS", "kafka:9092")

# ID constant pour ce process
DEVICE_ID = str(uuid.uuid4())

# Conditions d'arrêt
run = True
def _stop(*_):
    global run; run = False
for sig in (signal.SIGINT, signal.SIGTERM):
    signal.signal(sig, _stop)

# Producteur Kafka    
p = Producer({
    "bootstrap.servers": BOOTSTRAP,
    "enable.idempotence": True,
    "acks": "all",
    "linger.ms": 10,
    "batch.num.messages": 1000,
    "compression.type": "lz4",
})

# Données simulées
battery = random.randint(60, 100)
LAT = random.uniform(-90, 90)
LON = random.uniform(-180, 180)

def sample():
    global LAT, LON, battery
    bpm = max(40, min(160, random.randint(60,85) + random.randint(-8,15)))
    temp = round(random.uniform(36.2, 38.2), 1)
    alert = random.random() < ALERT_RATE or bpm < 45 or bpm > 140 or temp > 38.0 or battery < 15
    LAT = max(-90, min(90, LAT + random.uniform(-0.0005, 0.0005)))
    LON = max(-180, min(180, LON + random.uniform(-0.0005, 0.0005)))
    battery = max(0, battery - BATTERY_DECAY)
    if battery == 0:
        battery = random.randint(60, 100)  # recharge
    return {
        "ID": DEVICE_ID,
        "BPM": bpm,
        "Température": temp,
        "PourcentageBatterie": round(battery, 2),
        "Alerte": bool(alert),
        "Longitude": round(LON, 6),
        "Latitude": round(LAT, 6),
        "Timestamp": int(time.time())
    }

def delivery_report(err, msg):
    if err:
        print(f"deliver_error: {err}", file=sys.stderr)

def main():
    while run:
        rec = json.dumps(sample(), ensure_ascii=False).encode("utf-8")
        p.produce(TOPIC, value=rec, callback=delivery_report)
        p.poll(0)  # trigger callbacks
        time.sleep(INTERVAL)
    p.flush(5)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"fatal: {e}", file=sys.stderr); sys.exit(1)