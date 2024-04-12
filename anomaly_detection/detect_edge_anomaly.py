import faust
from settings import KAFKA_BROKER_URL, DETECTED_ANOMALIES_TOPIC, NETWORK_DATA_TOPIC

class Data(faust.Record, serializer='json'):
    device_id: str
    network_traffic: float
    timestamp: str


app = faust.App('anomaly_detection_app', broker=KAFKA_BROKER_URL)
network_data_topic = app.topic(NETWORK_DATA_TOPIC, value_type=Data)
anomalies_topic = app.topic(DETECTED_ANOMALIES_TOPIC, value_type=Data)


@app.agent(network_data_topic)
async def detect_anomaly(stream):
    async for event in stream:
        #if event.network_traffic > 80:  # Anomaly if traffic > 80
            print(f"Anomaly detected: {event}")
            await anomalies_topic.send(value=event)

if __name__ == '__main__':
    app.main()
