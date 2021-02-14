from pub_sub.publisher import Publisher
from threading import Thread
import threading
from pub_sub.subscriber import Subscriber
import time
import sys
import os

def start_listening(sub):
    sub.listen()


def main(image_folder):
    sub = Subscriber('deep-fashion-production', 'client_response-sub')
    thread = Thread(target=start_listening, kwargs={"sub": sub})
    thread.start()
    time.sleep(0.2)
    
    pub = Publisher('deep-fashion-production', 'client_request')
    
    for image in os.listdir(image_folder):
        img_path = image_folder + "/" + image
        pub.publish(img_path)
        
if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print('usage: python app.py path/to/image/folder')
        exit(0) 
    main(sys.argv[1])