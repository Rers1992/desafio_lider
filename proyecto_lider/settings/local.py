from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'djongo',
        'NAME': 'mongodb-local',
        'CLIENT': {
                'host': 'localhost',
                'port': 27017,
                'username': 'productListUser',
                'password': 'productListPassword',
                'authSource': 'admin',
        } 
        #'USER': 'productListUser',
        #'PASSWORD': 'productListPassword',
   }
}