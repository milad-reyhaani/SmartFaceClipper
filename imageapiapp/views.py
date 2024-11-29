import base64
from django.core.files.base import ContentFile
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import EmployeeImage
from .serializers import EmployeeImageSerializer
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
import pdb
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
import datetime
from datetime import datetime
import re
from .functions.DetectFace import crop_faces

static_images_folder = os.path.join(os.getcwd(), '', 'static', 'Images')

class ImageView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            if request.data.get('image_name'):
                image_name = request.data.get('image_name')
                # Your logic to fetch the image path based on image_name
                image_path = static_images_folder + f"\{image_name}.jpg"

                # Get the full path to the image
                #full_path = os.path.join(settings.MEDIA_ROOT, image_path)
                full_path = image_path

                # Get the file's status
                file_status = os.stat(full_path)
                
                os.name
                # Extract the modification time
                modified_time_timestamp = file_status.st_ctime

                # Convert the modification time to a human-readable format
                modified_time = datetime.fromtimestamp(modified_time_timestamp)

                # Read the image file and encode it as base64
                base64_image = crop_faces(full_path)
                    
                
                # Return the response as JSON
                return JsonResponse({
                    "ImageName": image_name,
                    "modified_time":modified_time,
                    "base64_image": base64_image,
                })
            else:
                # Return an error response if an exception occurs
                return JsonResponse({'error': 'image_name parameter is not provided.'}, status=500)
        except:
            return JsonResponse({'error': 'Employee image was not found'}, status=404)
    def post(self, request):
        # This method handles POST requests
        return self.get(request)
class ImageViewFilter(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            if request.data.get('from_date') and request.data.get('to_date'):

                # Extract from_date and to_date from the request body
                from_date_str = re.sub('/',"-",re.sub('\\\\',"-",request.data.get('from_date'))) 
                to_date_str = re.sub('/',"-",re.sub('\\\\',"-",request.data.get('to_date'))) 

                # Convert from_date and to_date strings to datetime objects
                from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
                to_date = datetime.strptime(to_date_str, '%Y-%m-%d')

                # Get the full path to the image
                #full_path = os.path.join(settings.MEDIA_ROOT, image_path)
                full_path = static_images_folder
                
                # Get the list of image files in the media directory
                image_files = [f for f in os.listdir(full_path) if f.endswith('.jpg') or f.endswith('.JPG')]

                # Initialize a dictionary to store base64-encoded image data
                image_data =[]

                # Iterate over each image file
                for image_file in image_files:
                    base64_image = None
                    # Get the full path to the image file
                    full_path_img = os.path.join(full_path, image_file)

                    # Get the modification time of the image file
                    modified_time = datetime.fromtimestamp(os.path.getctime(full_path_img))

                    # Check if the modification time falls within the specified date range
                    if from_date <= modified_time <= to_date:
                        # Read the image file in binary mode
                        base64_image = crop_faces(full_path_img)
                        if(base64_image):
                            ImageName = re.sub(".jpg","",image_file, flags=re.IGNORECASE)

                            # Store the base64-encoded image data in the dictionary
                            image_data.append({'ImageName': ImageName, "modified_time":modified_time,'base64_image': base64_image})
                        
                            
                            
                # Return the dictionary containing the base64-encoded image data as a JSON response
                return JsonResponse(image_data, safe=False)
            else:
                # Return an error response if an exception occurs
                return JsonResponse({'error': 'from_date parameter and to_date is not provided.'}, status=500)
        except Exception as e:
            # Return an error response if an exception occurs
            return JsonResponse({'error': str(e)}, status=500)
    def post(self, request):
        # This method handles POST requests
        return self.get(request)

class AllImages(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:

            # Get the full path to the image
            #full_path = os.path.join(settings.MEDIA_ROOT, image_path)
            full_path = static_images_folder
            
            # Get the list of image files in the media directory
            image_files = [f for f in os.listdir(full_path) if f.endswith('.jpg') or f.endswith('.JPG')]

            # Initialize a dictionary to store base64-encoded image data
            image_data =[]

            # Iterate over each image file
            for image_file in image_files:
                base64_image = None
                # Get the full path to the image file
                full_path_img = os.path.join(full_path, image_file)
                
                # Get the modification time of the image file
                modified_time = datetime.fromtimestamp(os.path.getctime(full_path_img))
                # Read the image file in binary mode
                base64_image = crop_faces(full_path_img)
                if(base64_image):
                    ImageName = re.sub(".jpg","",image_file, flags=re.IGNORECASE)
                    
                    # Store the base64-encoded image data in the dictionary
                    image_data.append({'ImageName': ImageName, "modified_time":modified_time,'base64_image': base64_image})
                    
                        
                        
            # Return the dictionary containing the base64-encoded image data as a JSON response
            return JsonResponse(image_data, safe=False)

        except Exception as e:
            # Return an error response if an exception occurs
            return JsonResponse({'error': str(e)}, status=500)