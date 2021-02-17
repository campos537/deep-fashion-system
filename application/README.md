# Client Application

this folder contains a simple client application that publish a folder of images to GooglePub/Sub and Kafka receiving the predict results as answer

## Usage

To use this repository please follow the steps below:

```
cd deep-fashion-system/application
# export the Gcloud credentials of your project
export GOOGLE_APPLICATION_CREDENTIALS=credentials.json 
python3.7 client_app.py path/to/image_folder path/to/config/file
```