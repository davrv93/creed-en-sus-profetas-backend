from .base import *

WSGI_APPLICATION = 'django_rv_apps.wsgi.prod_do.application'

DEBUG = True

USE_X_FORWARDED_HOST = True