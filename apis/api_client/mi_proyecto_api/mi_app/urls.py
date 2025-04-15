from django.urls import path
from .views import TaskListCreateView, TaskDetailView, UserListCreateView, UserDetailView, mark_task_completed

urlpatterns = [
    # Endpoints para Task
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    # Endpoints para User
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('tasks/<int:pk>/complete/', mark_task_completed, name='mark-task-completed'),
]