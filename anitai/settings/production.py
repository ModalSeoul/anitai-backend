"""
Base settings, extended by the dev/staging/production settings.
"""

import os
from django.utils.log import DEFAULT_LOGGING

DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
)))


MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'widget_tweaks',
    'corsheaders',
    'social.apps.django_app.default',
    'apps.landing',
    'apps.accounts',
    'apps.show',
    'apps.image',
    'apps.character',
    'apps.announcement'
)

# Domain configuration
SITE_SCHEMA = os.environ.get('SCHEMA', 'http')
SITE_DOMAIN = os.environ.get('FQDN', 'localhost')
FRONTEND_OAUTH_REDIRECT = 'http://local.izeni.net:9000/oauth/'

# 3rd party framework configuration
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'apps.accounts.authentication.NoCSRFSessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
    'PAGE_SIZE': 100,
}

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'anitai'),
        'USER': os.environ.get('DB_USER', 'anitai'),
        'PASSWORD': os.environ.get('DB_PASS', 'anitai'),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Auth Configuration
AUTH_USER_MODEL = 'accounts.EmailUser'
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'

# python-social-auth django settings
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = (
    'first_name', 'last_name', 'email')
USER_FIELDS = ('email',)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'izeni.django.accounts.pipelines.validate',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}
SOCIAL_AUTH_FACEBOOK_KEY = '1649988431884827'
SOCIAL_AUTH_FACEBOOK_SECRET = '143fb8c7bc682c44b6f6fbc3e98094c4'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '974923707135-9qgnbrpq4a72qecjtfricf9fbv1otv5h.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'koODPW6fIwJVI4-zHezApf7m'


########################################################################
# You will only rarely need to change anything below here.
########################################################################


class EmailSettings:
    HEADER_COLOR = "#03a9f4"  # Material Blue 500
    BG_COLOR = "#f5f5f5"  # Material Grey 100
    CONTENT_COLOR = "#ffffff"  # White
    HIGHLIGHT_COLOR = "#f5f5f5"  # Material Grey 100
    LOGO_URL = "https://i.imgur.com/w5uY0Vx.png"
    LOGO_ALT_TEXT = ""
    TERMS_URL = ""
    PRIVACY_URL = ""
    UNSUBSCRIBE_URL = ""
    FONT_CSS = 'font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'
    FONT_CSS_HEADER = 'font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;'


EMAIL = EmailSettings()
EMAIL_BACKEND = 'django_ses_backend.SESBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PORT = 587
EMAIL_HOST_USER = 'alaygrow@gmail.com'
EMAIL_HOST_PASSWORD = 'zugzwang17'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'admin@{}'.format('anitai.faith')

# General
MANAGERS = ADMINS = (
    ('anitai Admin', 'anitai+admin@izeni.com'),
)

IZENI = {
    'ADMIN': {
        'SITE_TITLE': "anitai backend",
    }
}

# Host names
INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = [SITE_DOMAIN]


# Logging
# The numeric values of logging levels are in the following table:
#
# CRITICAL    50
# ERROR       40
# WARNING     30
# INFO        20
# DEBUG       10
# NOTSET      0 [default]
#
# Messages which are less severe than the specified level will be
# ignored.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': DEFAULT_LOGGING['filters'],
    'formatters': {
        'default': {
            '()': 'logging.Formatter',
            'format': '[%(asctime)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'debug': {
            '()': 'logging.Formatter',
            'format': '[%(asctime)s] %(levelname)s - %(name)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['require_debug_false'],
        },
        'debug-console': {
            'level': 'INFO',  # DEBUG level here is *extremely* noisy
            'class': 'logging.StreamHandler',
            'formatter': 'debug',
            'filters': ['require_debug_true'],
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': '/var/log/anitai/django.log',
            'maxBytes': 1000000,  # 1MB
            'delay': True,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'debug-console', 'file'],
            'level': 'NOTSET',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'debug-console', 'file'],
            'level': 'NOTSET',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'debug-console', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}


# Caching
CACHES = {
    'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}
}


# Templates
from izeni.django import accounts
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'anitai', 'templates'),
            os.path.join(accounts.__path__[0], 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# password policies
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


########################################################################
# You shouldn't ever have to change anything below here.
########################################################################


# Static/Media
MEDIA_ROOT = '/var/media/anitai/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '/var/media/anitai/static'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'anitai', 'static'),
)


# URLs
ROOT_URLCONF = 'anitai.urls'


# ./manage.py runserver WSGI configuration
WSGI_APPLICATION = 'anitai.wsgi.application'


# i18n
USE_TZ = True
TIME_ZONE = 'America/Denver'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True


# Secrets
SECRET_KEY = ')l#q2y5p$6h^#tli8@!9#vwqck5&525vsg7m1*%qt%h43ifo0k'
