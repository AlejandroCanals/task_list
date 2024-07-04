from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
# Create your views here.


def task_list(request):
    tasks = Task.objects.all()
    return render(request,'app/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('task_list')
    
    else:
        form = TaskForm()
    return render(request,'app/add_task.html',{'form': form})


def update_task(request,task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'GET':
        return render (request, 'app/update_task.html',{'task': task})
    
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('task_list')
    else:
        form = TaskForm()
    return render(request,'app/update_task.html')
        

def delete_task(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'GET':
        return render(request, 'app/delete_task.html', {'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('task_list')
    
    return redirect('task_list')  


                <form action="{% url 'update_task' task.id %}" method="get" style="display: inline;">
                    {% csrf_token %}
                    <button type="submit">Update</button>
                </form>   
                <form action="{% url 'delete_task' task.id %}" method="get" style="display: inline;">
                    {% csrf_token %}
                    <button type="submit">Delete</button>
                </form>