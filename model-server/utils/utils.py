import json
import base64
import numpy as np
from utils.response_object import ResponseObject

def msg2img(stream_decoded):
    img = np.array(stream_decoded.get("img"), dtype=np.uint8)
    img_name = stream_decoded.get("image_name")
    return img, img_name

def result2msg(result, img_name):
    return ResponseObject(result, img_name).get_object()

def check_msg(result):
    stream = base64.decodebytes(result)
    stream_decoded = stream.decode()
    if 'cool' in stream_decoded:
        return result , "text"
    else:
        return json.loads(stream_decoded), "img"