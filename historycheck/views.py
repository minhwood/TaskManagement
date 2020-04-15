from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .responses.task_responses import TaskResponse
from django.shortcuts import get_object_or_404

from .models import Task

#responses Define
task_responses = TaskResponse()

@api_view(['GET'])
def list(request):
    task = Task.objects.all()
    return Response(task_responses.convertToResponse(task))

@api_view(['POST'])
def create(request):
    return Response("Post")