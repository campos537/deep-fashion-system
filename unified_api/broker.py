from unified_api.brokers.pubsub.subscriber import Subscriber
from unified_api.brokers.pubsub.publisher import Publisher

from unified_api.brokers.kafka.consumer import Consumer
from unified_api.brokers.kafka.producer import Producer

#from brokers.kafka import Kafka
from unified_api.utils.utils import valid_pubsub, valid_kafka
import threading
import base64
import time


class Giver:
    def __init__(self, giver):
        self.giver = giver
        self.valid = False

    def set_valid(self, valid):
        self.valid = valid

    def publish(self, message):
        self.giver.publish(message)


class Broker:
    def __init__(self, config):
        self.givers = []
        self.receivers = []
        self.config = config
        
        self.both = valid_pubsub(config) and valid_kafka(config)
        if valid_pubsub(config):
            self.givers.append(Giver(Publisher(config)))
            self.receivers.append(Subscriber(config))
        if valid_kafka(config):
            self.givers.append(Giver(Producer(config)))
            self.receivers.append(Consumer(config))
        


    def publish(self, message):
        for giver in self.givers:
            if giver.valid == True or not self.both:
                giver.publish(message)

    def listen(self):
        for receiver in self.receivers:
            t1 = threading.Thread(target=receiver.listen)
            t1.start()
        if self.both:
            self.validate()

    def get_message(self):
        for receiver in self.receivers:
            message = receiver.get_message()
            if (message is not None):
                return message

    def validate(self):
        for giver in self.givers:
            giver.publish(base64.urlsafe_b64encode("cool".encode()))
            timeout = time.time() + 10
            while True:
                mes = self.get_message()
                if mes is not None:
                    giver.valid = True
                    break
                if(time.time() > timeout):
                    timeout = 0
                    giver.valid = False
                    break