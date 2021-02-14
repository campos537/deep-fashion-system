import time
import uuid
from google.cloud import pubsub_v1
import numpy as np
import json
import base64
import cv2
import os 

class Subscriber:
    def __init__(self, project_id, subscription_id):
        self.subscriber = pubsub_v1.SubscriberClient()
        self.subscription_path = self.subscriber.subscription_path(project_id, subscription_id)
        self.futures = dict()
        
    def callback(self, message):
        if message is not None:
            stream = base64.decodebytes(message.data)
            stream_decoded = json.loads(stream.decode())
            print("Image name: ", stream_decoded.get("image_name"), " Class Predicted: ", stream_decoded.get("class"))
        message.ack()

    def listen(self):
        streaming_pull_future = self.subscriber.subscribe(self.subscription_path, callback=self.callback)
        print(f"Listening for messages on {self.subscription_path}..\n")

        with self.subscriber:
            try:
                streaming_pull_future.result()
            except TimeoutError:
                streaming_pull_future.cancel()