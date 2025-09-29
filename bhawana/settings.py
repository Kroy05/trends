# settings.py (production-ready, Vercel friendly) - UPDATED
from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# load local .env in development only (optional)
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# Security / env-driven
# -----------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "dev-secret-key-please-change"  # only fallback for local development
)

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# -----------------------
# ALLOWED_HOSTS & CSRF_TRUSTED_ORIGINS
# Provide ALLOWED_HOSTS as comma-separated env var in Vercel for production:
#   ALLOWED_HOSTS=bhwanahandloom.com,www.bhwanahandloom.com,bhwanahandloom.vercel.app
# If env var not present, we include common defaults (localhost, vercel).
# Note: ".vercel.app" will match any vercel subdomain, but we also add the explicit vercel app domain.
# -----------------------
_default_hosts = "127.0.0.1,localhost,bhwanahandloom.com,www.bhwanahandloom.com,bhwanahandloom.vercel.app,.vercel.app"
ALLOWED_HOSTS = [
    h.strip() for h in os.getenv("ALLOWED_HOSTS", _default_hosts).split(",") if h.strip()
]

# CSRF trusted origins require scheme (https). Set CSRF_TRUSTED_ORIGINS env or use defaults below.
_default_csrf = "https://bhwanahandloom.com,https://www.bhwanahandloom.com,https://bhwanahandloom.vercel.app"
CSRF_TRUSTED_ORIGINS = [
    u.strip() for u in os.getenv("CSRF_TRUSTED_ORIGINS", _default_csrf).split(",") if u.strip()
]

# -----------------------
# Application definition
# -----------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store",
    "contact",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # serve static
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bhawana.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bhawana.wsgi.application"

# -----------------------
# Database (Postgres)
# -----------------------
# Provide POSTGRES_URL in env (e.g. postgres://user:pass@host:port/dbname)
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("POSTGRES_URL"),
        conn_max_age=int(os.getenv("DB_CONN_MAX_AGE", 600)),
        ssl_require=os.getenv("DB_SSL_REQUIRE", "True").lower() == "true",
    )
}

# -----------------------
# Password validation
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------
# Internationalization
# -----------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = os.getenv("TIME_ZONE", "UTC")
USE_I18N = True
USE_TZ = True

# -----------------------
# Static files (whitenoise)
# -----------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]  # if you keep static/ in project root
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -----------------------
# Security headers & cookies (production)
# -----------------------
# If behind proxy (Vercel), use X-Forwarded-* headers
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Enforce HTTPS in production (enable via env)
if os.getenv("SECURE_SSL_REDIRECT", "True").lower() == "true":
    SECURE_SSL_REDIRECT = True
else:
    SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "True").lower() == "true"
CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE", "True").lower() == "true"
X_FRAME_OPTIONS = "DENY"

# HSTS - enable after verifying HTTPS works
SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", 0))
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.getenv("SECURE_HSTS_INCLUDE_SUBDOMAINS", "False").lower() == "true"
SECURE_HSTS_PRELOAD = os.getenv("SECURE_HSTS_PRELOAD", "False").lower() == "true"

# -----------------------
# Other settings
# -----------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Simple logging to console (adjust as needed)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
    },
}
