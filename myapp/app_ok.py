from django.db.models import Q

from myapp.models import UploadedSelfie

# List of file names
file_names = ['salah-767485100_8ius3qH.jpg', 'ice_d8g7ZKD.jpgdia/']

# Fetch images
images = []
for file_name in file_names:
    image = UploadedSelfie.objects.filter(Q(img__exact=file_name))
    images.append(image)

# Display images
for image in images:
    print(image.img.url)