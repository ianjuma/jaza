"""
WSGI config for django-rest.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/opt/domains/morpheus-web')

os.environ["DJANGO_SETTINGS_MODULE"] = "jaza.settings"

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
