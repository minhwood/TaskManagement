from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.TextField(max_length=1200)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField()