# Client Application

this folder contains a simple client application that publish a folder of images to Google Pub/Sub and receives the predicted results

## Usage

To use this repository please follow the steps below:

```
cd deep-fashion-system/application
# export the Gcloud credentials of your project
export GOOGLE_APPLICATION_CREDENTIALS=credentials.json 
python3.7 client_app.py path/to/image_folder
```