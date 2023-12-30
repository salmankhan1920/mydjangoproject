from django.urls import path
from . import views



urlpatterns = [

    path("upload_selfie/", views.upload_selfie, name='upload_selfie'),
    path('get_images/', views.get_images, name='get_images'),
    path('backend/', views.backend.as_view(), name='backend'),
    path('done/', views.done, name='done'),
    path('testing/', views.testing),
    path('media/<path:path>', views.serve_media, name='media'),
   # path('media/selfies/<str:image_name>', views.serve_media)

] 