from rest_framework import generics
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Vista para la raíz del proyecto
def home(request):
    return HttpResponse("<h1>Bienvenido a la API</h1>")

# Vistas para Task
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed', 'title']

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(['POST'])
def mark_task_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return Response({'status': 'Tarea completada'})

# Vistas para User
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer