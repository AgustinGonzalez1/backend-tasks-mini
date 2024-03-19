from rest_framework import viewsets, permissions, status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = TaskSerializer
  
  @action(detail = True, methods = ['post'])
  def completed(self, request, pk = None):
    task = self.get_object()
    task.completed = not task.completed
    task.save()
    return Response({
      'status': 'task done' if task.completed else 'task undone' 
    }, status = status.HTTP_200_OK)