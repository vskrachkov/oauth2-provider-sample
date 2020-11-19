from pathlib import Path

from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = []

DJANGO_CORE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "oauth2_provider",
    "rest_framework",
]

PROJECT_APPS = [
    "users",
    "oauth2server",
]

INSTALLED_APPS = DJANGO_CORE_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "oauth2_server_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": Path(__file__).resolve().parent.parent.parent / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

LOGIN_URL = "/admin/login/"

AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.DjangoModelPermissions"],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}

CORS_ALLOW_ALL_ORIGINS = True


OAUTH2_PROVIDER = {
    "ACCESS_TOKEN_EXPIRE_SECONDS": 60 * 60 * 24,
    "REFRESH_TOKEN_EXPIRE_SECONDS": 60 * 60 * 24,
    "REFRESH_TOKEN_GRACE_PERIOD_SECONDS": 60 * 2,
    "AUTHORIZATION_CODE_EXPIRE_SECONDS": 60 * 60,
    "ROTATE_REFRESH_TOKEN": True,
    "REQUEST_APPROVAL_PROMPT": "auto",
    "ACCESS_TOKEN_GENERATOR": "oauth2server.generators.generate_access_token",
    "REFRESH_TOKEN_GENERATOR": "oauth2server.generators.generate_access_token",
    "OAUTH2_SERVER_CLASS": "oauthlib.oauth2.Server",
    "OAUTH2_VALIDATOR_CLASS": "oauth2_provider.oauth2_validators.OAuth2Validator",
    "CLIENT_ID_GENERATOR_CLASS": "oauth2server.generators.ClientIdGenerator",
    "CLIENT_SECRET_GENERATOR_CLASS": "oauth2server.generators.ClientSecretGenerator",
    "SCOPES_BACKEND_CLASS": "oauth2server.scopes_backend.SettingsScopes",
    "ALLOWED_REDIRECT_URI_SCHEMES": ["http", "https"],
    "ERROR_RESPONSE_WITH_SCOPES": True,
    "PKCE_REQUIRED": False,
}
