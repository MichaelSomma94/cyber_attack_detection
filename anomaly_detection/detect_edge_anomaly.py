import faust
from settings import KAFKA_BROKER_URL, DETECTED_ANOMALIES_TOPIC, NETWORK_DATA_TOPIC
from ae_models import ae_process_data
class Data(faust.Record, serializer='json'):
    id: str
    features: list
    log: dict

app = faust.App('anomaly_detection_app', broker=KAFKA_BROKER_URL)
network_data_topic = app.topic(NETWORK_DATA_TOPIC, value_type=Data)
anomalies_topic = app.topic(DETECTED_ANOMALIES_TOPIC, value_type=Data)


@app.agent(network_data_topic)
async def detect_anomaly(stream):
    async for event in stream:
            #print(event)
            detection_dict = ae_process_data(event)
        #if event.network_traffic > 80:  # Anomaly if traffic > 80
            print(f"Anomaly detected: {detection_dict}")
            await anomalies_topic.send(value=detection_dict)

if __name__ == '__main__':
    app.main()
