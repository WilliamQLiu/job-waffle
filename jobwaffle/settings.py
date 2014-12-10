"""
Django settings for jobwaffle project.

Run using: python manage.py runserver --settings=jobwaffle.settings.local

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from __future__ import absolute_import  # Allow explicit relative imports

import os
import socket
#import dj_database_url  # for heroku


from .secret import SECRET_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, \
    EMAIL_USE_TLS, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, \
    EMAIL_PORT

SECRET_KEY = SECRET_KEY

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#BASE_DIR = os.path.dirname(__file__)
#PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
#TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['www.jobwaffle.com', 'jobwaffle.com']

if socket.gethostname() in (ALLOWED_HOSTS):  # 'www.jobwaffle.com'
    DEBUG = False
else:
    DEBUG = True
    TEMPLATE_STRING_IF_INVALID = "INVALID EXPERSSION: %s"
    # For complex templates, this exp prints incorrect fields for debugging

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

# Email Settings from secret.py
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT

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

SITE_ID = 1  # For django-allauth

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# auth and allauth settings
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'publish_stream'],
        'METHOD': 'js_sdk'  # instead of 'oauth2'
    }
}

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

LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'jobwaffle.urls'

WSGI_APPLICATION = 'jobwaffle.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {

         #Postgresql - On Ubuntu Server w/Postgresql - For Testing Only
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jobwaffle',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',

        # Will's Mac, Local Developer settings with MySQL - local
        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'jobwaffle',
        #'USER': 'root',
        #'PASSWORD': '',
        #'HOST': '127.0.0.1',

    }
}

# Parse database configuration from $DATABASE_URL
#DATABASES['default'] =  dj_database_url.config()  # For Heroku

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"

MEDIA_ROOT = (
    os.path.join(os.path.dirname(BASE_DIR), "media")
    )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#STATIC_ROOT = '/var/www/jobwaffle/static/'
STATIC_ROOT = (
    os.path.join(os.path.dirname(BASE_DIR), "static")
    )
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "job-waffle", "static"),
    )


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    #'compressor.finders.CompressorFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "job-waffle", "templates"),
    #os.path.join(PROJECT_ROOT, "templates"),
)

# List of callables that know how to import templates from various sources
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
    )

# Django Rest Framework
REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Authentication identifies the credentials that the request was made wtih
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.

    # Permissions run at the start of the view; checks authentication info in the
    # request.user and request.auth properties
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
