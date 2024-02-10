from django.urls import path
from .views import ToDoListView

urlpatterns = [
    path('', ToDoListView.task_list, name='task_list'),
    path('add/', ToDoListView.add_task, name='add_task'),
    path('delete/<int:task_id>/', ToDoListView.delete_task, name='delete_task'),
    path('save/', ToDoListView.save_tasks, name='save_tasks'),
    path('load/', ToDoListView.load_tasks, name='load_tasks'),
]
