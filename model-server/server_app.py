from classifier.classifier import Classifier
from utils.utils import msg2img, result2msg, check_msg
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
            decoded, type_ = check_msg(msg)
            if type_ == "img":
                img, name = msg2img(decoded)
                broker.publish(result2msg(classifier.predict(img), name))
            else:
                broker.publish(decoded)

def main(config_):
    config = Config(config_)
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