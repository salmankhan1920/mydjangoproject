from django.urls import path
from . import views



urlpatterns = [

    path("upload_selfie/", views.upload_selfie, name='upload_selfie'),
    path('get_images/', views.get_images, name='get_images'),
    path('testing/', views.testing),
    path('media/<path:path>', views.serve_media, name='media'),
    path('site-admin/' , views.site_admin, name='site-admin'),
    path('navbar/', views.navbar, name='navbar'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<int:page>', views.gallery, name='gallery'),
    path('test/', views.test, name='test'),
    path('login/' , views.login_dashboard, name='login')
   

] 