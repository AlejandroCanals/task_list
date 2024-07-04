from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('add/', TaskCreateView.as_view(), name='add_task'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
    path('delete/<int:task_id>/', TaskDeleteView.as_view(), name='delete_task'),
]