import os
from pathlib import Path

# Define la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-inseguro-una_clave_secreta_segura_y_unica'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST Framework
    'mi_app',  # Tu aplicación
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # Middleware para la seguridad y manejo de solicitudes
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de las URLs principales
ROOT_URLCONF = 'mi_proyecto_api.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Directorios adicionales para plantillas (si los tienes)
        'APP_DIRS': True,  # Busca plantillas dentro de las aplicaciones
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

# Configuración del servidor WSGI
WSGI_APPLICATION = 'mi_proyecto_api.wsgi.application'

# Configuración de la base de datos (Oracle Database)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle', 
        'NAME': 'FREE',          # Nombre del servicio de Oracle (por defecto, FREE para Oracle 23c Free)
        'USER': 'SYSTEM',        # Usuario de Oracle Database
        'PASSWORD': 'user_super', # Contraseña del usuario
        'HOST': 'localhost',       # Dirección del servidor (localhost si está en tu máquina)
        'PORT': '1521',            # Puerto de Oracle Database (por defecto, 1521)
    }
}

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuración de claves primarias automáticas
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de depuración y hosts permitidos
DEBUG = False 
# Cambia a True para desarrollo y asegúrate de no dejarlo en producción
# Cambia a False para producción y asegúrate de configurar ALLOWED_HOSTS adecuadamente

ALLOWED_HOSTS = ['tu-dominio.com', '127.0.0.1', 'localhost']  # Hosts permitidos

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Cambia esto según el dominio de tu frontend
    "http://127.0.0.1:3000",
]