# API Django/Flask

Proyecto de ejemplo que implementa una API utilizando Django y/o Flask.

## Estructura del proyecto

- mi_app/ y mi_proyecto_api/: Código fuente de la aplicación.
- staticfiles/: Archivos estáticos.
- db.sqlite3: Base de datos SQLite del proyecto.
- manage.py: Script de gestión de Django.

## Requisitos

- Python 3.x
- Django (instalar con pip install django)
- (Opcional) Flask si tienes partes del proyecto con Flask

## Cómo ejecutar

1. Instala las dependencias:
   `ash
   pip install django
   ` 
2. Realiza migraciones (si es necesario):
   `ash
   python manage.py migrate
   ` 
3. Ejecuta el servidor de desarrollo:
   `ash
   python manage.py runserver
   ` 
4. Accede a la API en http://localhost:8000

## Notas

- Si tienes un entorno virtual, recuerda activarlo antes de instalar dependencias.
- No subas la carpeta .venv ni archivos sensibles al repositorio.
