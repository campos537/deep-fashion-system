import json
import base64
import numpy as np
from utils.response_object import ResponseObject

def msg2img(message):
    stream = base64.decodebytes(message)
    stream_decoded = json.loads(stream.decode())
    img = np.array(stream_decoded.get("img"), dtype=np.uint8)
    img_name = stream_decoded.get("image_name")
    
    return img, img_name

def result2msg(result, img_name):
    return ResponseObject(result, img_name).get_object()