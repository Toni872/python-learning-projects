import os
from django.core.wsgi import get_wsgi_application

# Configura el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto_api.settings')

application = get_wsgi_application()