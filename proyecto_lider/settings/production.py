from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['proyecto-lider.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'djongo',
        'NAME': 'mongodb-local',
        'USER': '',
        'PASSWORD': '',
        'HOST':'',
        'DATABASE_PORT':'27017',
   }
}
