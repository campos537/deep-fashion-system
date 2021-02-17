import cv2
import asyncio
import numpy as np

class Classifier:

    def __init__(self, config):

        if config["framework"] == "ONNX":
            self.net = cv2.dnn.readNetFromONNX(config["trained_file"])
        else:
            self.net = cv2.dnn.readNet(
                config["trained_file"], config["config_file"], config["framework"])

        self.labels = self.set_config_value(config.get("labels"), ())
        self.setBackend(self.set_config_value(config.get("backend"), 3))
        self.setTarget(self.set_config_value(config.get("target"), 0))

        self.scalefactor = self.set_config_value(
            config.get("scalefactor"), 1.0)
        self.size = config.get("input_size")
        self.mean = self.set_config_value(config.get("mean"), ())
        self.swapRB = self.set_config_value(config.get("swapRB"), False)
        self.crop = self.set_config_value(config.get("crop"), False)
        self.ddepth = self.set_config_value(config.get("ddepth"), cv2.CV_32F)

    def set_config_value(self, value, default):
        return value if value is not None else default

    # Convert the raw result to the string labels
    def process_output(self, out):
        out = out.flatten()
        classId = np.argmax(out)
        return self.labels[classId]

    def setBackend(self, backend):
        self.net.setPreferableBackend(backend)

    def setTarget(self, target):
        self.net.setPreferableTarget(target)

    def predict(self, img):
        # Preprocess the image to the network needs
        blob = cv2.dnn.blobFromImage(
            img, self.scalefactor, (self.size[1],self.size[2]), self.mean, self.swapRB, self.crop, self.ddepth)
        self.net.setInput(blob)
        out = self.net.forward()
        return self.process_output(out)