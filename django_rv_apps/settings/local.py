from .base import *

WSGI_APPLICATION = 'django_rv_apps.wsgi.local.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'davrv93',
        'USER': 'admin',
        'PASSWORD': 'Admin123!',
        # Or an IP Address that your DB is hosted on
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
