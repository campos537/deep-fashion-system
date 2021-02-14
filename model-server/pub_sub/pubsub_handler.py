from pub_sub.publisher import Publisher
from pub_sub.subscriber import Subscriber


class PubSubHandler:
    def __init__(self, config):
        self.sub = Subscriber(config)

    def start(self):
        self.sub.listen()
