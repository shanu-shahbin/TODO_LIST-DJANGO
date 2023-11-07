from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo


def home(request):
    task_all = Todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Todo(title=name, date=date, priority=priority)
        task.save()
    return render(request, 'home.html', {'task_all': task_all})


def delete(request, taskid):
    task = Todo.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'task':task})
