from pub_sub.pubsub_handler import PubSubHandler
from config import Config
import sys


def main(model_path):
    config = Config(model_path)
    print("Model Framework: ", config.get("framework"), " Model Labels: ", config.get("labels"))
    pubsub = PubSubHandler(config)
    pubsub.start()

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print("usage: python app.py path/to/model/")
        exit(0)
    main(sys.argv[1])