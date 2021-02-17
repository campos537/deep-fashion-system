from threading import Thread
from config import Config
from utils.stream_object import StreamObject
import threading
import time
import sys
import os
import base64
sys.path.append(os.path.abspath('../'))
from unified_api.broker import Broker
from utils.utils import get_result


def start_listening(broker):
    broker.listen()

def process_request(broker):
    while(True):
        msg = broker.get_message()
        if msg is not None:
            print(get_result(msg))
            
def main(image_folder, config):
    broker = Broker(Config(config))
    thread = threading.Thread(target=start_listening, kwargs={"broker": broker})
    thread.start()
    thread2 = threading.Thread(target=process_request, kwargs={"broker": broker})
    thread2.start()

    for image in os.listdir(image_folder):
        img_path = image_folder + "/" + image
        broker.publish(StreamObject(img_path).get_object())


if __name__ == '__main__':
    if not len(sys.argv) == 3:
        print('usage: python app.py path/to/image/folder path/to/config/file')
        exit(0)
    main(sys.argv[1], sys.argv[2])
