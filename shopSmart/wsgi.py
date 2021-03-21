"""
WSGI config for shopSmart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

#print(sys.path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopSmart.settings')


application = get_wsgi_application()
