from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json
import face_recognition
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

image_folder = os.path.join(BASE_DIR, "media", "selfies")



 
# function to check if face is found in the image
@sync_to_async
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



class SelfieConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['uuid']
        self.room_group_name = 'upload_selfie_%s' % self.room_name
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['message']:  
          if text_data_json['message'] == 'Hello Server!':
             # Send message to room group
             await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'connection success'
            }
        )
        if text_data_json['message'] == 'filename':
            self.image_name = text_data_json['filename']
            print('image nameee', self.image_name)
            await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'function is running'
           }
        ) 
            result = await get_images(self.image_name)

            print(result)

            if result:
                print(result)
                await self.send(text_data=json.dumps({'message':result}))
            else:
                print('hi')
    

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))



# function to check if face is found in the image
'''
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

            '''