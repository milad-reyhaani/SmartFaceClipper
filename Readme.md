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
  