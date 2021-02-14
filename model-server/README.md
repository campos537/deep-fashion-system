# Model Server Application

this folder contains a simple but robust model server application that uses Google PubSub as a message broker.

## Usage

To use this repository you will first need to have an json file with the model configuration and a [model](https://github.com/campos537/simple-fashion-classifier) trained for that

Create the json file following the example below:

```
{
    "project_id": "your-project-id",
    "topic_id": "your-topic-id",
    "subscription_id": "your-subscription-id", 
    "framework": "ONNX",
    "trained_file": "path/to/model/model.onnx",
    "backend": 3,
    "target": 0,
    "input_size": [1,32,32,1],
    "scalefactor": 1.0,
    "swapRB": true,
    "labels": ["angle-boot","bag","coat","dress","pullover",
        "sandal", "shirt", "sneaker", "t-shirt", "trouser"]
}
```

Then pass the configuration json as an argument:

```
cd deep-fashion-system/model-server
export GOOGLE_APPLICATION_CREDENTIALS=credentials.json 
python3.7 server_app.py path/to/configuration/file
```