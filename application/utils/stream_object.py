import base64
import cv2
import numpy as np
import json

class StreamObject:
    def __init__(self, img_path):
        img = cv2.imread(img_path)
        img_list = img.tolist()
        
        self.obj_ = {}
        self.obj_["img"] = img_list
        self.obj_["image_name"] = img_path
    
    def get_object(self):
        return base64.urlsafe_b64encode(json.dumps(self.obj_).encode())