from unified_api.brokers.pubsub.subscriber import Subscriber
from unified_api.brokers.pubsub.publisher import Publisher

from unified_api.brokers.kafka.consumer import Consumer
from unified_api.brokers.kafka.producer import Producer

#from brokers.kafka import Kafka
from unified_api.utils.utils import valid_pubsub, valid_kafka


class Broker:
    def __init__(self, config):
        self.giver = None
        self.receiver = None
        if valid_pubsub(config):
            self.giver = Publisher(config)
            self.receiver = Subscriber(config)
            self.broker_type = "pubsub"

        elif valid_kafka(config):
            self.giver = Producer(config)
            self.receiver = Consumer(config)
            self.broker_type = "kafka"

    def publish(self, message):
        self.giver.publish(message)

    def listen(self):
        self.receiver.listen()

    def get_message(self):
        return self.receiver.get_message()
