def valid_pubsub(config):
    if (config.get("topic_id") is not None and config.get("project_id") is not None
            and config.get("subscription_id") is not None):
        return True
    return False

def valid_kafka(config):
    if config.get("bootstrap_server") is not None and config.get("port") is not None:
        return True
    return False