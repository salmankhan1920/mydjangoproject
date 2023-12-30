import face_recognition
import os

# Load the selfie image
selfie_image = face_recognition.load_image_file(
    "/home/syedyasin/Desktop/projects/face_recognition/selfie/doors_mastergrain-204129462.JPG"
)

selfie_encoding = face_recognition.face_encodings(selfie_image)


# Load and encode the images in the images folder
image_folder = "/home/syedyasin/Desktop/projects/face_recognition/images"
matching_images = []


if len(selfie_encoding) > 0:
    selfie_encoding = selfie_encoding[0]

    for image_file in os.listdir(image_folder):
        image = face_recognition.load_image_file(os.path.join(image_folder, image_file))
        image_encoding = face_recognition.face_encodings(image)

        if len(image_encoding) > 0:
            image_encoding = image_encoding[0]
            # Compare the face encodings
            results = face_recognition.compare_faces([selfie_encoding], image_encoding)

            if results[0] == True:
                matching_images.append(image_file)
        else:
            print("No faces detected in the image")
else:
    print("No face detected in the selfie")


# List the matching images
print("Matching images: ", matching_images)
