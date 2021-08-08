from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from tasks.models import Tasks




def index(request):
    td = Tasks.objects.all()
    return render(request, 'index.html',{'tdl':td})


def add(request):
    
    if request.method == "POST":
        
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        t = Tasks(tasks_name=title,tasks_details=desc)
        t.save()
        messages.success(request, 'Your task added')
        return redirect('/addtask')
    else:
        return render(request, 'addtask.html')

def madone(request, id):
        tasks = Tasks.objects.get(pk=id)
        tasks.delete()
        return redirect('/')