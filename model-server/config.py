import json

def Config(config_path):
    with open(config_path) as config_file:
        return json.load(config_file)
    