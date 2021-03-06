"""
Django settings for ShopSenseMovie project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import dirname, abspath

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DJANGO_ROOT = os.environ.get('DJANGO_ROOT', dirname(dirname(abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oq7qju_04yevkg0mgu^7+b!2a%)fy3!q_n-)9+c5iu+9s26taz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.movie',
    'rest_framework',
    'django_tables2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ShopSenseMovie.urls'

WSGI_APPLICATION = 'ShopSenseMovie.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
import dj_database_url

DATABASES = {'default': dj_database_url.config()}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#     }
# }

try:
  from local_settings import *
except Exception as e:
  pass

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(DJANGO_ROOT, 'final_static')

STATIC_URL = '/static/'

# URL prefix for admin assets files -- CSS, JavaScript and images.
ADMIN_MEDIA_PREFIX = '/assets/admin/'

# Additional locations of assets files.
STATICFILES_DIRS = (
    os.path.join(DJANGO_ROOT, 'static'),
    os.path.join(DJANGO_ROOT, 'templates'),
)

# List of finder classes that know how to find assets files in various
# locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request'
)


MEDIA_ROOT = os.path.join(DJANGO_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'
# ######### END MEDIA CONFIGURATION
