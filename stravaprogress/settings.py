"""
Django settings for stravaprogress project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
from os import environ, path
BASE_DIR = path.dirname(path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5u&z*8dsn6z$+0hg=v0gwvz_oc(@1-%)1&3q2ma=25oefy8we$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'core',
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

ROOT_URLCONF = 'stravaprogress.urls'

WSGI_APPLICATION = 'stravaprogress.wsgi.application'


# Auth
# http://python-social-auth.readthedocs.org/

AUTHENTICATION_BACKENDS = (
    'social.backends.strava.StravaOAuth',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'core.pipeline.save_profile',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_STRAVA_KEY = environ.get('SOCIAL_AUTH_STRAVA_KEY', '')
SOCIAL_AUTH_STRAVA_SECRET = environ.get('SOCIAL_AUTH_STRAVA_SECRET', '')
# TODO: Figure out if necessary
# SOCIAL_AUTH_STRAVA_SCOPE = ['view_private']


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {}
environ.setdefault('DATABASE_URL', 'postgres://127.0.0.1:5432/%s' % environ.get('USER', 'postgres'))
DATABASES['default'] = dj_database_url.config()


# Template
# TODO: Remove when not using django templates any longer

TEMPLATE_DIRS = (
    path.join(BASE_DIR, 'core/templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)


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
