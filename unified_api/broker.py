from unified_api.brokers.pubsub.subscriber import Subscriber
from unified_api.brokers.pubsub.publisher import Publisher

from unified_api.brokers.kafka.consumer import Consumer
from unified_api.brokers.kafka.producer import Producer

#from brokers.kafka import Kafka
from unified_api.utils.utils import valid_pubsub, valid_kafka
import threading
import base64
import time
import gc

class Broker:
    def __init__(self, config):
        self.givers = []
        self.receivers = []
        self.config = config
    
        if valid_pubsub(config):
            self.givers.append(Publisher(config))
            self.receivers.append(Subscriber(config))
        if valid_kafka(config):
            self.givers.append(Producer(config))
            self.receivers.append(Consumer(config))

    def publish(self, message):
        for giver in self.givers:
            giver.publish(message)

    def listen(self):
        for receiver in self.receivers:
            t1 = threading.Thread(target=receiver.listen)
            t1.start()
        
    def get_message(self):
        for receiver in self.receivers:
            message = receiver.get_message()
            if (message is not None):
                return message