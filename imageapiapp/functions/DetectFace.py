import cv2
import base64

def crop_faces(image_path, min_padding=100):
    # Load the image
    image = cv2.imread(image_path)

    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale (required by the face detection model)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    scaleFactorZarib = 1.1
    
    while scaleFactorZarib < 2.0:
        faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactorZarib, minNeighbors=5, minSize=(30, 30))

        # Check if no face is detected
        if len(faces) == 0:
            return None
        elif len(faces) == 1:
        # Crop faces
            for (x, y, w, h) in faces:
                (x, y, w, h) = faces[0]

                # Calculate the size of the detected face
                face_width = w
                face_height = h

                # Calculate the padding based on the size of the detected face
                padding = max(min_padding, int(max(face_width, face_height) * 0.5))  # Set padding to at least min_padding
                
                # Calculate the new coordinates for cropping with 50 pixels around
                x_new = max(0, x - padding)
                y_new = max(0, y - padding)
                w_new = min(image.shape[1], w + 2 * padding)
                h_new = min(image.shape[0], h + 2 * padding)

                # Crop the region of interest (face with additional 50 pixels around) from the original image
                face_roi = image[y_new:y_new+h_new, x_new:x_new+w_new]
                
                # Convert the cropped face image to base64 format
                _, buffer = cv2.imencode('.jpg', face_roi)
                base64_image = base64.b64encode(buffer).decode('utf-8')

                
                # Save the cropped face to a file (optional)
                #cv2.imwrite('D:\\New folder (6)\\'+filename, face_roi)
                
                return base64_image
            
        elif len(faces) > 1:
            scaleFactorZarib += 0.1