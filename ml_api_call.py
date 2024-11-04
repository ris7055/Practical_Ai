from dotenv import load_dotenv
import os
import requests

# Load environment variables from a .env file
load_dotenv()

endpoint = os.getenv("AZURE_VISION_ENDPOINT")
subscription_key = os.getenv("AZURE_VISION_SUBSCRIPTION_KEY")

if not endpoint or not subscription_key:
    raise EnvironmentError("Please set AZURE_VISION_ENDPOINT and AZURE_VISION_SUBSCRIPTION_KEY as environment variables.")

# API URL and request parameters
analyze_url = f"{endpoint}/vision/v3.1/analyze"
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}
params = {
    "visualFeatures": "Categories,Description,Color"
}

# Example image URL
image_url = "https://miro.medium.com/v2/resize:fit:3840/1*0ubYRV_WNR9iYrzUAVINHw.jpeg"
data = {"url": image_url}

# Make the request to the Azure Vision API
response = requests.post(analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()
analysis = response.json()
print("Analysis results:", analysis)

