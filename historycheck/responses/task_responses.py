from ..models import Task
from django.db.models.query import QuerySet

class TaskResponse(object):

    def convertToResponse(self, tasks):
        if type(tasks) is QuerySet:
            return self.__toResponses(tasks)
        else:
            return self.__toResponse(tasks)

    def __toResponse(self, task):
        return {
            "task_name": task.task_name,
            "task_description": task.task_description,
            "accepted": task.accepted,
            "created-at": task.created_at
        }
    
    def __toResponses(self, tasks):
        result = []
        for task in tasks:
            result.append(self.__toResponse(task))
        return result
        