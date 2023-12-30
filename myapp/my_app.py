import face_recognition
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

image_folder = os.path.join(BASE_DIR, "media", "images")






# function to check if face is found in the image
def get_images(image_url):
    file_path = image_folder + "/" + image_url


    matching_images = []

    # Load the selfie image
    selfie_image = face_recognition.load_image_file(file_path)

    selfie_encoding = face_recognition.face_encodings(selfie_image)

    if len(selfie_encoding) > 0:
        selfie_encoding = selfie_encoding[0]

        for image_file in os.listdir(image_folder):
            image = face_recognition.load_image_file(
                os.path.join(image_folder, image_file)
            )
            image_encoding = face_recognition.face_encodings(image)

            if len(image_encoding) > 0:
                image_encoding = image_encoding[0]
                # Compare the face encodings
                results = face_recognition.compare_faces(
                    [selfie_encoding], image_encoding
                )

                if results[0] == True:
                    matching_images.append(image_file)
                    

            else:
                print("No faces detected in the image")
        return matching_images
        
      
    else:
        print("No face detected in the selfie")


# List the matching images
#print("Matching images: ", matching_images)




get_images()
print(matching_images)