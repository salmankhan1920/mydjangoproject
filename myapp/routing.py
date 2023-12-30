from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/upload_selfie/<str:uuid>/', consumers.SelfieConsumer.as_asgi()),
]
