"""
WSGI config for Smokey Peeks project.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smokey_peeks.settings')

application = get_wsgi_application()
