from dataclasses import dataclass, field
from typing import List, Dict
from kafka import KafkaProducer
import json
import random
from time import sleep
from settings import BROKER_URL


# defing a rigid schema for the streamed data

@dataclass
class Data:
    id: str
    features: List[float] = field(default_factory=list)
    log: Dict[str, any] = field(default_factory=dict)



producer = KafkaProducer(bootstrap_servers=[BROKER_URL],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))


# different edge devices
devices = ['device1', 'device2', 'device3', 'device4', 'device5']

def generate_data():
    for _ in range(5):  # generate 10 data points for each device
        for device in devices:
            features = [float(f"{random.gauss(0.5, 0.1):.2f}") for _ in range(10)]  # 10 features
            log_data = {
                "temperature": random.randint(20, 50),
                "status": random.choice(["normal", "warning", "critical"])
            }
            data = Data(
                id=f"{device}_{random.randint(1000, 9999)}",
                features=features,
                log=log_data
            )
            yield data.__dict__

def send_to_kafka():
    for data in generate_data():
        producer.send('network_data_top', value=data)
        print("Sent data:", data)
        sleep(1)

if __name__ == "__main__":
    send_to_kafka()


# export PYTHONPATH=/Users/michiundslavki/Dropbox/JR/SerWas/cyber_attack_detection:$PYTHONPATH


