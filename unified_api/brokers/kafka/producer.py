from kafka import KafkaProducer
import time


class Producer:
    def __init__(self, config):
        bootstrap_server = config.get(
            "bootstrap_server") + ":" + config.get("port")
        self.topic_id = config.get("topic_id")
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_server, api_version=(0,10))

    def publish(self, data):
        self.producer.send(self.topic_id, data)
        time.sleep(0.01)
