"""
Django settings for bhawana project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# .env file ko load karne ke liye (local development ke liye)
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECRET KEY aur DEBUG ---
# Yeh Vercel ya .env file se values lega
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 
    'your-default-development-secret-key-for-local-use'
)
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# --- ALLOWED HOSTS ---
# Vercel aur local host ko allow karein
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'contact',
]

# --- MIDDLEWARE ---
# Whitenoise middleware ko sahi jagah par rakhein
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bhawana.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bhawana.wsgi.application'

# --- DATABASE SETUP ---
# Yeh code cloud database (Neon, Supabase, etc.) use karega
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('POSTGRES_URL'),
        conn_max_age=600
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- STATIC FILES SETUP FOR VERCEL ---
# Yeh Vercel par aapki CSS/JS files ko serve karega
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'