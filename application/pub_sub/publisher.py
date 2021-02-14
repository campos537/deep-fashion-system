import time
from google.cloud import pubsub_v1
from utils.stream_object import StreamObject
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
    
    def publish(self, img_path):
        data = StreamObject(img_path).get_object()
        self.futures.update({data: None})
        future = self.publisher.publish(self.topic_path, data)
        self.futures[data] = future
        future.add_done_callback(self.get_callback(future, data))
        while self.futures:
            time.sleep(0.001)
    