from django.contrib import admin
from .models import Tasks,Goals

# Register your models here.

@admin.register(Tasks)
class adminTasks(admin.ModelAdmin): 
    list_display = ['id', 'tasks_name', 'tasks_details', 'task_date']
admin.site.register(Goals)
