from kafka import KafkaConsumer

class Consumer:
    def __init__(self, config):
        bootstrap_server = config.get(
            "bootstrap_server") + ":" + config.get("port")
        self.consumer = KafkaConsumer(config.get(
            "subscription_id"), bootstrap_servers=bootstrap_server, api_version=(0, 10), 
                                      auto_offset_reset='earliest', enable_auto_commit=True, group_id="test")
        self.messages = []

    def get_message(self):
        if len(self.messages) > 0:
            mes = self.messages.pop(0)
            return mes

    def listen(self):
        for message in self.consumer:
            self.messages.append(message.value)
