import time
import uuid
import asyncio
from google.cloud import pubsub_v1


class Subscriber:
    def __init__(self, config):
        self.subscriber = pubsub_v1.SubscriberClient()
        self.subscription_path = self.subscriber.subscription_path(
            config["project_id"], config["subscription_id"])
        self.futures = dict()
        self.lock = False
        self.messages = []
    
    def get_message(self):
        if len(self.messages) > 0:
            mes = self.messages.pop(0)
            return mes
    
    def callback(self, message):
        self.messages.append(message.data)
        message.ack()
        
    def listen(self):
        streaming_pull_future = self.subscriber.subscribe(
            self.subscription_path, callback=self.callback)
        print(f"Listening for messages on {self.subscription_path}..\n")

        with self.subscriber:
            try:
                print(streaming_pull_future.result())
            except TimeoutError:
                streaming_pull_future.cancel()