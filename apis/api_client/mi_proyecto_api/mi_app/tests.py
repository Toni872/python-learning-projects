from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title="Prueba", description="Descripción de prueba")
        self.assertEqual(task.title, "Prueba")