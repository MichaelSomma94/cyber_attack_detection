from kafka import KafkaProducer
import json
import random
from time import sleep
#from config import settings


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

devices = ["device_1", "device_2", "device_3", "device_4", "device_5"]

for _ in range(10):  # Send 100 messages for each device
    for device in devices:
        data = {
            "device_id": device,
            "network_traffic": random.random() * 100,  # Random traffic data
            "timestamp": "2024-04-09T12:00:00"
        }
        producer.send('network_data_top', value=data)
        sleep(1)  # Sleep for a second to simulate real-time data flow
