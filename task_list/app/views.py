from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'app/task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'app/add_task.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'app/update_task.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(View):
    template_name = 'app/delete_task.html'
    success_url = reverse_lazy('task_list')

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['task_id'])
        return render(request, self.template_name, {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['task_id'])
        task.delete()
        return redirect(self.success_url)
