"""
    Will's settings file for working on project locally.
    Sets debug to true, uses local db, activates developer tools

    Run: $python manage.py runserver --settings=jobwaffle.settings.production

"""

from __future__ import absolute_import  # Allow explicit relative imports

from .base import *
import dj_database_url  # for heroku

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['www.jobwaffle.com', 'jobwaffle.com']

DATABASES = {
    'default': {

         #Postgresql - On Ubuntu Server w/Postgresql - For Testing Only
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jobwaffle',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',

    }
}


# AWS SETTINGS
AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'  #django-storage
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'  #django-storage

AWS_STORAGE_BUCKET_NAME = 'jobwaffle'
AWS_PRELOAD_METADATA = True  # collectstatic to upload changed (instead of all)

STATIC_URL = 'https://jobwaffle.s3.amazonaws.com/static/'
ADMIN_MEDIA_PREFIX = 'https://jobwaffle.s3.amazonaws.com/static/admin/'
MEDIA_URL = 'https://jobwaffle.s3.amazonaws.com/media/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.contrib.auth.context_processors.auth',
    # Required for django-allauth template tags
    "django.core.context_processors.request",
    # Required for django-allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # templates look nice
    'employer',
    'applicant',
    'rest_framework',  # DjangoRestFramework
    #'debug_toolbar',  # Activate Django Debug Toolbar
    # The Django sites framework is required
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.twitter',
)