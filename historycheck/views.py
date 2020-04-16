from rest_framework import generics, mixins
from .models import Task
from historycheck.responses.task_serializers import TaskSerializer
from django.db.models import Q

from datetime import datetime

class TaskCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookupfield = 'pk'
    serializer_class = TaskSerializer

    #for search
    def get_queryset(self):
        qs = Task.objects.all()
        search = self.request.GET.get("search")
        if (search) is not None:
            qs = qs.filter(
                Q(task_name__icontains=search)|
                Q(task_description__icontains=search)
            ).distinct()
        return qs

    #action when perform create action
    def perform_create(self, serializer):
        serializer.save(created_at=datetime.now())

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TaskRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookupfield = 'pk'
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return Task.objects.get(pk=pk)