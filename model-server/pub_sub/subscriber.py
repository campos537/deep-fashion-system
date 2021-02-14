import time
import uuid
from google.cloud import pubsub_v1
import numpy as np
import json
import base64
import asyncio
from classifier.classifier import Classifier
from pub_sub.publisher import Publisher
import cv2
import os 

images = []

class Subscriber:
    def __init__(self, config):
        self.subscriber = pubsub_v1.SubscriberClient()
        self.subscription_path = self.subscriber.subscription_path(config["project_id"], config["subscription_id"])
        self.pub = Publisher(config["project_id"], config["topic_id"])
        self.classifier = Classifier(config)
        self.futures = dict()
        
    def callback(self, message):
        stream = base64.decodebytes(message.data)
        stream_decoded = json.loads(stream.decode())
        
        img = np.array(stream_decoded.get("img"), dtype=np.uint8)
        img_name = stream_decoded.get("image_name")
        
        self.pub.publish(self.classifier.predict(img),img_name)
        message.ack()

    def listen(self):
        streaming_pull_future = self.subscriber.subscribe(self.subscription_path, callback=self.callback)
        print(f"Listening for messages on {self.subscription_path}..\n")

        with self.subscriber:
            try:
                streaming_pull_future.result()
            except TimeoutError:
                streaming_pull_future.cancel()
                