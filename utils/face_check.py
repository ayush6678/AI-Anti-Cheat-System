import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def count_people(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Load the pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Return the number of faces detected
    return len(faces)

def compare_images(image_path1, image_path2):
    # Read the images
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # Count people in each image
    people_count1 = count_people(image1)
    people_count2 = count_people(image2)

    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Resize images to have the same dimensions
    height = min(gray1.shape[0], gray2.shape[0])
    width = min(gray1.shape[1], gray2.shape[1])
    gray1 = cv2.resize(gray1, (width, height))
    gray2 = cv2.resize(gray2, (width, height))

    # Compute SSIM between the two images
    similarity_index, _ = ssim(gray1, gray2, full=True)

    return [similarity_index, people_count1, people_count2]
