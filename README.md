# Deep Fashion System
This repository contains a solution of client/server to run an Deep Learning Classification model and gets the answer at the client side, it was implemented using Google Pub/Sub, OpenCV, Numpy and other technologies.

# Usage 
first you will have to create a project in the Gcloud platform an then go PubSub and create 2 topics, 1 will deal with request communication with the server and the other one with the answer from the server, then adjust the parameters depending on your project_id, subscription_ids and topic_ids. After adjusting the Gcloud parameters follow the instructions of `application` and `model-server`folders.

## Requirements Installation
```
python3.7 -m pip install -r requirements.txt
```