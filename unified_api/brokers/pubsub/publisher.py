import time
import uuid
from google.cloud import pubsub_v1

class Publisher:
    def __init__(self, config):
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(config.get("project_id"), config.get("topic_id"))
        self.futures = dict()
        
    def get_callback(self ,f, data):
        def callback(f):
            try:
                self.futures.pop(data)
            except:
                print("Please handle {}.".format(f.exception()))
        return callback
    
    def publish(self, data):
        #data = ResponseObject(result, img_name).get_object()
        self.futures.update({data: None})
        if data is not None:
            future = self.publisher.publish(self.topic_path, data)
        self.futures[data] = future
        future.add_done_callback(self.get_callback(future, data))
        while self.futures:
            time.sleep(1)