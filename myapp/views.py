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
    
    # Check if the image has been successfully saved
    '''
    if UploadedSelfie.objects.filter(selfie=image).exists():
        response_data = {'message': 'Image uploaded successfully'}
        return JsonResponse(response_data)
    else:
        response_data = {'message': 'Image not saved'}
        return JsonResponse(response_data)
        '''

   else:

       return render(request, "upload.html")


def get_images(request):
    image_name = request.session.get("image_name", "")
    print(image_name)
    if image_name:
        return HttpResponse("function successfull")
    else:
        return render(request, "get_images.html")


"""

def backend(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('image upload successfull')
    else:
        form = ImageForm()
    return render(request, 'backend.html', {'form':form})
"""


class backend(FormView):
    template_name = "backend.html"
    form_class = UploadForm
    success_url = "/done/"

    def form_valid(self, form):
        for each in form.cleaned_data["attachments"]:
            print("each", each)
            print("form", form)
            Images.objects.create(image=each)
        return super(backend, self).form_valid(form)


def done(request):
    return render(request, "done.html")



def testing(request):
    images = UploadedSelfie.objects.all()

    return render(request, 'testing.html', {'images':images})




def serve_media(request, path):
    return static.serve(request, path, document_root=settings.MEDIA_ROOT)