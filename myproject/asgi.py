"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.sessions import SessionMiddlewareStack
from myapp import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": SessionMiddlewareStack(URLRouter(
            routing.websocket_urlpatterns
        ))
    
        # Add other protocols and routers here as needed
    })
