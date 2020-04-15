from django.urls import path, include, re_path
from .views import TaskRUDView, TaskCreateView

app_name = 'historycheck'

urlpatterns = [
    path('', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/', TaskRUDView.as_view(), name='task-rud')
]