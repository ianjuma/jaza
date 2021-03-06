from os.path import join, dirname
from dotenv import load_dotenv
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP


dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


"""
Django settings for thinkster_django_angular_boilerplate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "$6(x*g_2g9l_*g8peb-@anl5^*8q!1w)k&e&2"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG   = os.environ.get('DEBUG', False)
SITE_ID = 1

TEMPLATE_DEBUG = True


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'compressor',
    'authentication',
    'agents',
    'products',
    'utils',
    'jaza'
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'jaza.urls'

WSGI_APPLICATION = 'jaza.wsgi.application'

SLEUTH_INTERFACE = 'http://162.13.138.91:8082/'
CRUNCH_INTERFACE = 'http://10.181.64.226:8081/'

API_KEY = '3147102a5544a8a8a499ad042adf2b627b82819a55e7259c08b89c805e2aef0b'
SLEUTH_API_KEY = 'f7f4f428-fe82-4d7e-b9e3-15dbffa073a2'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'morpheus_web',
        'USER'     : 'morpheus_netuser',
        'PASSWORD' : 'KJShq2&#1_qgss12asg@42',
        'HOST'     : '10.181.194.210',
        'PORT'     : '3306'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.LimitOffsetPagination',
    ),
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['airtime.jaza.co.ke']

# AUTH_USER_MODEL = 'authentication.User'

PWD = os.path.dirname(os.path.realpath(__file__))
SITE_ROOT = os.path.join(PWD, "../")
COUNTRY_INFO_FILE = SITE_ROOT + 'data/countrylist.csv'

LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'formatters': {
    'standard': {
      'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
      'datefmt' : "%d/%b/%Y %H:%M:%S"
      },
    },
  'handlers': {
    'null': {
      'level':'DEBUG',
      'class':'django.utils.log.NullHandler',
      },
    'logfile': {
      'level':'DEBUG',
      'class':'logging.handlers.RotatingFileHandler',
      'filename': '/var/tmp/log/morpheus-web/application.log',
      'maxBytes': 2147483648,
      'backupCount': 10,
      'formatter': 'standard',
      },
    'console':{
      'level':'INFO',
      'class':'logging.StreamHandler',
      'formatter': 'standard'
      },
    },
  'loggers': {
    'django': {
      'handlers':['console'],
      'propagate': True,
      'level':'WARN',
      },
    'django.request': {
      'handlers': ['logfile'],
      'level': 'DEBUG',
      'propagate': False,
      },
    '': {
      'handlers': ['console', 'logfile'],
      'level': 'DEBUG',
      },
    }
}

try:
    from jaza.settings_dev import *
except ImportError:
    pass
