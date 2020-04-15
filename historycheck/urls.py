from django.urls import path, include
from . import views

app_name = 'historycheck'

urlpatterns = [
    path('', views.list, name='list'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create')
]