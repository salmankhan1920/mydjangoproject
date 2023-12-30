import face_recognition
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

image_path = os.path.join(BASE_DIR, "media", "selfies")


"""
# Load the selfie image

selfie_image = face_recognition.load_image_file(image_path)

selfie_encoding = face_recognition.face_encodings(selfie_image)

"""


# function to check if face is found in the image
def check_selfie(image_url):
    file_path = image_path + "/" + image_url
    if os.path.exists(file_path):
        # Load the selfie image
        selfie_image = face_recognition.load_image_file(file_path)

        selfie_encoding = face_recognition.face_encodings(selfie_image)

        if len(selfie_encoding) > 0:
            return True

        else:
            return False
    else:
        print("file does not exist")
