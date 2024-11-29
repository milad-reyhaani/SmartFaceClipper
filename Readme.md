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
Username, Email address and Password. Once created, you can log in to the Django admin panel or use the superuser credentials for additional API functionalities.

- Run below command to apply any migration:
```
python manage.py migrate
```

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
### 1- http://127.0.0.1:8000/token/
Generate a JWT token for authentication to access other endpoints.
### 2- http://127.0.0.1:8000/singleimage/
Process an image by providing its name in the request body, returning the cropped image as a base64 string.

#### Sample Use Case
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

### 3- http://127.0.0.1:8000/modified_time_query/
Crop multiple image files based on their modified time.
#### Sample Use Case
```
import requests
import base64
import os

# Step 1: Get Access Token
url_token = "http://127.0.0.1:8000/token/"
token_payload = {
    "username": "user",
    "password": "password"
}
response_token = requests.post(url_token, json=token_payload)
response_token.raise_for_status()  # Ensure request was successful
access_token = response_token.json().get("access")

# Step 2: Set Authorization Header
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Step 3: Query Data
url_query = "http://127.0.0.1:8000/modified_time_query/"
body = {
    "from_date": "2024/11/01",
    "to_date": "2024/11/29"
}
response_query = requests.post(url_query, json=body, headers=headers)
response_query.raise_for_status()
data = response_query.json()

# Step 4: Process Each User's Image
output_directory = r"D:\Images"
os.makedirs(output_directory, exist_ok=True)  # Ensure output directory exists

for user in data:
    # Decode base64 data
    binary_image_data = base64.b64decode(user["base64_image"])
    
    # Save as JPEG
    image_name = user["ImageName"]
    file_path = os.path.join(output_directory, f"{image_name}.jpg")
    with open(file_path, "wb") as image_file:
        image_file.write(binary_image_data)
    
    print(f"Image saved at: {file_path}")
```
#### Notes:
- Replace "username" and "password" with the credentials of the account created in the previous section.
- Modify the from_date and to_date for batch processing, you should specify the time you would like to target your images.
- The cropped images will be saved in the specified directory (e.g., D:\Images).
- You can use the generated base64 strings directly in your automation environment or save them as image files.

### 4- http://127.0.0.1:8000/allimages/
Crop all image files in the `\static\Images` directory.
#### Sample Use Case
```
import requests
import base64
import os

# Step 1: Get Access Token
url_token = "http://127.0.0.1:8000/token/"
token_payload = {
    "username": "user",
    "password": "password"
}
response_token = requests.post(url_token, json=token_payload)
response_token.raise_for_status()  # Ensure the request was successful
access_token = response_token.json().get("access")

# Step 2: Set Authorization Header
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Step 3: Fetch User Data
url_images = "http://127.0.0.1:8000/allimages/"
response_images = requests.get(url_images, headers=headers)
response_images.raise_for_status()
user_data = response_images.json()

# Step 4: Process Each User's Image
output_directory = r"D:\Images"
os.makedirs(output_directory, exist_ok=True)  # Ensure output directory exists

for user in user_data:
    # Decode base64 data
    binary_image_data = base64.b64decode(user["base64_image"])
    
    # Save as JPEG
    image_name = user["ImageName"]
    file_path = os.path.join(output_directory, f"{image_name}.jpg")
    with open(file_path, "wb") as image_file:
        image_file.write(binary_image_data)
    
    print(f"Image saved at: {file_path}")
```
#### Notes:
- Replace "username" and "password" with the credentials of the account created in the previous section.
- The /allimages/ endpoint processes every image in the \static\Images directory.
- The cropped images will be saved in the specified directory (e.g., D:\Images).
- You can use the generated base64 strings directly in your automation environment or save them as image files.