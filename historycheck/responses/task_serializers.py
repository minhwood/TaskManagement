from rest_framework import serializers

from historycheck.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'pk',
            'task_name',
            'task_description',
            'accepted',
            'created_at',
        ]
        read_only_fields = ['created_at']
    
    def validate_task_name(self, value):
        if (len(value) < 10):
            raise serializers.ValidationError("Task Name must be longer than 10 characters")
        return value