from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.db.models import Q

def index(request):
    query = request.GET.get('q')
    tasks = Task.objects.filter(title__icontains=query) if query else Task.objects.all().order_by('due_date')

    form = TaskForm()

    if request.method == 'POST':
        if 'add_task' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        elif 'toggle' in request.POST:
            task = Task.objects.get(id=int(request.POST.get('toggle')))
            task.completed = not task.completed
            task.save()
            return redirect('/')
        elif 'delete' in request.POST:
            Task.objects.get(id=int(request.POST.get('delete'))).delete()
            return redirect('/')

    return render(request, 'index.html', {'form': form, 'tasks': tasks})


def edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit.html', {'form': form, 'task': task})