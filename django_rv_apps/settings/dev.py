from .base import *

WSGI_APPLICATION = 'django_rv_apps.wsgi.prod_do.application'

DEBUG = True

#gUSE_X_FORWARDED_HOST = True
#FORCE_SCRIPT_NAME = '/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'davrv93',
        'USER': 'davrv93',
        'PASSWORD': 'Davrv123',
        # Or an IP Address that your DB is hosted on
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
