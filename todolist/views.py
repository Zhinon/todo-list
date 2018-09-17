from django.shortcuts import render
from django.utils import timezone
from .models import Task, Prioridad, Estate
from .forms import TaskForm

# Create your views here.


def task_list(request):
    tasklist = Task.objects.order_by('published_date')
    return render(request, 'todolist/todolist.html', {'tasks': tasklist})

def task_new(request):
    form = TaskForm()
    return render(request, 'todolist/task_edit.html', {'form': form})
