# <snippet_imports>
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import requests
import io

# </snippet_imports>

'''
Prerequisites:

1. Install the Custom Vision SDK. Run:
pip install --upgrade azure-cognitiveservices-vision-customvision

2. Create an "Images" folder in your working directory.

3. Download the images used by this sample from:
https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/CustomVision/ObjectDetection/Images

This sample looks for images in the following paths:
<your working directory>/Images/fork
<your working directory>/Images/scissors
<your working directory>/Images/test
'''

# Replace with your Azure endpoint and subscription keys.
ENDPOINT = "https://eilearn-prediction.cognitiveservices.azure.com/"
prediction_key = "3d36c550ca484853b4f94a01293abf01"
prediction_resource_id = "/subscriptions/e3ad05bf-f0e5-4124-967f-5a245408d944/resourceGroups/Eilearn/providers/Microsoft.CognitiveServices/accounts/Eilearn-Prediction"
# </snippet_creds>

# <snippet_auth>
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
# </snippet_auth>

# <snippet_create>
publish_iteration_name = "Iteration2"

base_image_location = r"C:\Users\jaddh\code_projects\EILearn\map_layers\popp_karte\images\tiles\15\16642\10965.jpg"

# Open the sample image and get back the prediction results.

with open(base_image_location, mode="rb") as test_data:
    results = predictor.detect_image("2d90f277-ac1c-490c-9b14-34fee8011de7", publish_iteration_name, test_data)

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100), prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height)
    
    # Load the image as bytes
    with open(base_image_location, mode="rb") as image_file:
        image_bytes = image_file.read()

    # Display the image with rectangles
    image = Image.open(io.BytesIO(image_bytes))

    probability_limit = 0.5
    
    for prediction in results.predictions:
        left = prediction.bounding_box.left * image.width
        top = prediction.bounding_box.top * image.height
        width = prediction.bounding_box.width * image.width
        height = prediction.bounding_box.height * image.height
        
        # Calculate the color intensity based on probability

        if (prediction.probability) > probability_limit:
            rect = patches.Rectangle((left, top), width, height, linewidth=1, edgecolor=(1, 0, 0,), facecolor='none')

        # Add the patch to the Axes
        plt.gca().add_patch(rect)

    # Display the image with rectangles
    plt.imshow(image)
    plt.axis('off')
    plt.show()