"""
ASGI config for websockettest project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from tester.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websockettest.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            URLRouter(
                [path('ws/tester/<str:room_name>', ChatConsumer.as_asgi())]
            )
        )
    }
)
