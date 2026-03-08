"""
ASGI config for Smokey Peeks project.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smokey_peeks.settings')

application = get_asgi_application()
