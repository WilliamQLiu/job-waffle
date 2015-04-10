"""
Django settings for jobwaffle project.

Run: $python manage.py runserver --settings=jobwaffle.settings.base

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from __future__ import absolute_import  # Allow explicit relative imports

import os
import socket
from urlparse import urlparse

import dj_database_url  # for heroku
from .secret import MY_SECRET_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, \
    EMAIL_USE_TLS, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, \
    EMAIL_PORT

SECRET_KEY = MY_SECRET_KEY

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

#DEBUG = True
DEBUG = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#STATIC_ROOT = '/var/www/jobwaffle/static/'

if DEBUG:
    STATIC_ROOT = (
        os.path.join(os.path.dirname(BASE_DIR), "job-waffle", "static")
        )
    STATIC_URL = '/static/'
    ALLOWED_HOSTS = ['*']  # Make it work on local

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/var/www/example.com/media/"

    MEDIA_ROOT = (
        os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "media")
        )

    #STATICFILES_DIRS = (
    #    os.path.join(os.path.dirname(BASE_DIR), "job-waffle", "static"),
    #    )

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://example.com/media/", "http://media.example.com/"
    MEDIA_URL = '/media/'

else:

    # For Heroku
    DATABASE_URL='postgres://:@localhost/jobwaffle'
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
    #DATABASES['default'] =  dj_database_url.config(default=DATABASE_URL)

    #ALLOWED_HOSTS = ['www.jobwaffle.com', 'jobwaffle.com']
    ALLOWED_HOSTS = '*'
    STATIC_URL = 'https://jobwaffle.s3.amazonaws.com/static/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'  #django-storage
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'  #django-storage

    AWS_STORAGE_BUCKET_NAME = 'jobwaffle'
    AWS_PRELOAD_METADATA = True  # collectstatic to upload changed (instead of all)

    ADMIN_MEDIA_PREFIX = 'https://jobwaffle.s3.amazonaws.com/static/admin/'
    MEDIA_URL = 'https://jobwaffle.s3.amazonaws.com/media/'





# Settings for Local Dev

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Postgres
        'NAME': 'jobwaffle',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': ''
    }
}

'''

# Settings for Docker
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        #'HOST': 'db',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
'''

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Email Settings from secret.py
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT

SITE_ID = 2  # For django-allauth, can't be 1 (example.com)

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


LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'jobwaffle.urls'

WSGI_APPLICATION = 'jobwaffle.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Added Logging - https://docs.djangoproject.com/en/1.7/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}




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
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated'  # Must be Authenticated to login
        #'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # templates look nice
    'haystack',
    'employer',
    'applicant',
    'rest_framework',  # DjangoRestFramework
    'debug_toolbar',  # Activate Django Debug Toolbar
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


# Celery
BROKER_URL = 'redis://127.0.0.1:6379/0'
BROKER_TRANSPORT = 'redis'
# Access our database and pull out tasks at scheduled times and send to queue
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

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
    "django.core.context_processors.debug",  # for Debug
    # Required for django-allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)


# Every change in models will launch the elasticsearch 'update_index'
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


# AWS SETTINGS
AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY

es = urlparse(os.environ.get('SEARCHBOX_URL') or 'http://127.0.0.1:9200/')

port = es.port or 80

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': es.scheme + '://' + es.hostname + ':' + str(port),
        'INDEX_NAME': 'haystack',
    },
}

if es.username:
    HAYSTACK_CONNECTIONS['default']['KWARGS'] = {"http_auth": es.username + ':' + es.password}

