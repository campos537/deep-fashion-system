import time
import uuid
from google.cloud import pubsub_v1
import numpy as np
import base64
import cv2
import os 

class Publisher:
    def __init__(self, project_id, topic_id):
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(project_id, topic_id)
        self.futures = dict()
        
    def get_callback(self ,f, data):
        def callback(f):
            try:
                self.futures.pop(data)
            except:
                print("Please handle {}.".format(f.exception()))
        return callback

    def process_image(self, img_path):
        img = cv2.imread(img_path)
        final = base64.b64encode(img)
        return final
    
    def publish(self, img_path):
        data = self.process_image(img_path)
        self.futures.update({data: None})
        future = self.publisher.publish(self.topic_path, data)
        self.futures[data] = future
        future.add_done_callback(self.get_callback(future, data))
        while self.futures:
            time.sleep(1)
    