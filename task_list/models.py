from django.db import models


class Task_Status(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    

class Task(models.Model):
    path_file = models.CharField(max_length=255)
    status = models.ForeignKey(Task_Status, on_delete=models.CASCADE)
    parent_task = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    