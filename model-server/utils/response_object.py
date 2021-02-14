import base64
import json

class ResponseObject:
    def __init__(self, class_, image_name):
        
        self.obj_ = {}
        self.obj_["class"] = class_
        self.obj_["image_name"] = image_name
    
    def get_object(self):
        return base64.urlsafe_b64encode(json.dumps(self.obj_).encode())