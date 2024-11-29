# SmartFaceClipper

This project is a Python-based application built with Django and OpenCV for face detection and cropping. It takes an input image, detects the face(s) using OpenCV's face recognition capabilities, and generates a base64-encoded string of the cropped face image.

## Key Features
- Face detection using OpenCV.
- Crops the detected face(s) from the input image.
- Converts cropped images to base64 format for easy integration into web or API-based solutions.
- Built with Django for robust backend processing.
- **JWT authentication** for secure access to API endpoints.

## Use Cases
- Profile photo processing.
- Secure identity verification.
- Face-based content filtering.

## Getting Started
Clone the repository, follow the setup instructions, and deploy it locally or on a server to get started.

# Installation
## Prerequisites
- Python 3.8 and above  
- Install the following dependencies:  
  ```
  pip install Django
  pip install python-dotenv
  pip install djangorestframework
  pip install djangorestframework-simplejwt
  pip install opencv-python
  pip install Pillow
  ```
- To access the Django admin panel or perform administrative tasks, create a superuser:
```
python manage.py createsuperuser 
```

Follow the prompts to provide:
Username
Email address
Password
Once created, you can log in to the Django admin panel or use the superuser credentials for additional API functionalities.
- Finally, run your Django application:
```
python manage.py runserver
```

## Image directory
Place all the images you want to crop in the following directory of your project:
```
\static\Images
```

## Endpoints
- http://127.0.0.1:8000/token/
Generate a JWT token for authentication to access other endpoints.
- http://127.0.0.1:8000/singleimage/
Process an image by providing its name in the request body, returning the cropped image as a base64 string.

### Sample Use Case
```
import requests
import base64

# Step 1: Get access token
url = "http://127.0.0.1:8000/token/"
payload = {"username": "user", "password": "password"} 
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
response_data = response.json()

# Extract the access token
access_token = response_data.get('access')
token = f"Bearer {access_token}"

# Step 2: Post request with image name
headers2 = {
    "Authorization": token,
    "Content-Type": "application/json"
}

body = {
    "image_name": "example" 
}

response2 = requests.post("http://127.0.0.1:8000/singleimage/", headers=headers2, json=body)

# Extract base64 image data from the response
user_data = response2.json()
base64_image_data = user_data.get('base64_image')

# Step 3: Decode base64 and save as JPEG
binary_image_data = base64.b64decode(base64_image_data)
file_path = r"D:\124.jpg"

with open(file_path, "wb") as file:
    file.write(binary_image_data)

print(f"Image saved at: {file_path}")
```
#### Notes:
- Replace "username" and "password" with the credentials of the account created in the previous section.
- Replace "example" in the body with the name of the image file you want to crop.
- The cropped image will be saved in the specified directory (e.g., D:\124.jpg).
- You can use the generated base64 string in your automation environment.
