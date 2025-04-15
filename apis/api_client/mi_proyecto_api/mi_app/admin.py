from django.contrib import admin
from .models import Task

# Registro del modelo Task en el panel de administración
admin.site.register(Task)