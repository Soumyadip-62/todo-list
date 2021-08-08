from django.db import models

# Create your models here.
class Tasks(models.Model):
    tasks_name = models.CharField(max_length=30)
    tasks_details = models.CharField(max_length=90)
    task_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tasks_name
    
class Goals(models.Model):
    g_name = models.CharField(max_length=30)
    g_details = models.CharField(max_length=90)
    g_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    def __str__(self):
        return self.g_name
    
