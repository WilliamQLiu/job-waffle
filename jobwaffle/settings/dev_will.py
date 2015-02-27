"""
    SUMMARY
    Will's settings file for working on project locally.
    Sets debug to true, uses local db, activates developer tools

    DATABASE
    Start local postgresql DB server: $pg_ctl start
    Access local postgresql DB through shell: $psql
        List all databases using: # \list
        List all tables in the current database: # \dt
        Sample command:# CREATE DATABASE jobwaffle;
        Quit: \q

    DJANGO
    Run: $python manage.py runserver --settings=jobwaffle.settings.dev_will
    Syncdb: $python manage.py migrate --settings=jobwaffle.settings.dev_will
    Collectstatic: $python manage.py collecstatic

"""

from __future__ import absolute_import  # Allow explicit relative imports

from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

#ALLOWED_HOSTS = ['www.jobwaffle.com', 'jobwaffle.com']

'''
DATABASES = {
    'default': {

        #Postgresql
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jobwaffle',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',

    }
}
'''

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

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
