from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import SelfieForm, ImageForm
from .selfie import check_selfie

# from .my_app import get_images
from django.views.generic.edit import FormView
from .forms import UploadForm
from .models import Images, UploadedSelfie

#to serve static files
from django.conf import settings
from django.views import static

from django.core.paginator import Paginator


#pagination classes


# Create your views here.


def upload_selfie(request):
   if request.method == "POST":
    # Handle the uploaded image here
    image = request.FILES['image']
    #getting image_name
    image_name = image.name
    # Process the image and save it to the database
    selfie_model = UploadedSelfie.objects.create(selfie=image)
    selfie_model.save()
    if check_selfie(image_name):
       response_data = {'message': 'Face found'}
       return JsonResponse(response_data)
    else:
        response_data = {'message': 'No face'}
        return JsonResponse(response_data)

   else:

       return render(request, "upload.html")


def get_images(request):
    image_name = request.session.get("image_name", "")
    print(image_name)
    if image_name:
        return HttpResponse("function successfull")
    else:
        return render(request, "get_images.html")






def testing(request):
    images = UploadedSelfie.objects.all()

    return render(request, 'testing.html', {'images':images})



#to serve static files to users
def serve_media(request, path):
    return static.serve(request, path, document_root=settings.MEDIA_ROOT)





#to upload images in the admin databse
def site_admin(request):
    if request.method == 'POST':
       for f in request.FILES.getlist('file'):  # Assuming the file input name is 'file'
          instance = Images(image=f)  # Replace file_field with your actual file field
          instance.save()
       response_data = {'message':'images successfully saved'}
       return JsonResponse(response_data)
    else:
        return render(request, 'site-admin.html')




def navbar(request):
    return render(request, 'navbar.html')




def gallery(request):
    image_list = Images.objects.all().order_by('-uploaded_at')   # Assuming Images is the model for your images
    paginator = Paginator(image_list, 10)  # Show 10 images per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery.html', {'page_obj': page_obj, 'paginator':paginator})




def test(request):
    return render(request, 'test.html')