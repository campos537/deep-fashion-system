from classifier.classifier import Classifier
from utils.utils import msg2img, result2msg
import threading
from config import Config
import sys, os
sys.path.append(os.path.abspath('../'))

from  unified_api.broker import Broker

def start_listening(broker):
    broker.listen()
    
def process_request(broker, classifier):
    while(True):
        msg = broker.get_message()
        if msg is not None:
            img, name = msg2img(msg)
            broker.publish(result2msg(classifier.predict(img), name))

def main(model_path):
    config = Config(model_path)
    print("Model Framework: ", config.get("framework"), " Model Labels: ", config.get("labels"))
    
    broker = Broker(config)
    classifier = Classifier(config)
    
    thread = threading.Thread(target=start_listening, kwargs={"broker": broker})
    thread.start()
    thread = threading.Thread(target=process_request, kwargs={"broker": broker, "classifier": classifier})
    thread.start()

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print("usage: python app.py path/to/model/")
        exit(0)
    main(sys.argv[1])