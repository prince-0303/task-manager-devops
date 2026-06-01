from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from .tasks import send_task_notification

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        task = serializer.save()
        send_task_notification.delay(task.id, self.request.user.username)