from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
import json

class ToDoListView:
    @staticmethod
    def task_list(request):
        tasks = Task.objects.all()
        return render(request, 'todo_app/task_list.html', {'tasks': tasks})

    @staticmethod
    def add_task(request):
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('task_list')
        else:
            form = TaskForm()
        return render(request, 'todo_app/add_task.html', {'form': form})

    @staticmethod
    def delete_task(request, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('task_list')

    @staticmethod
    def save_tasks(request):
        tasks = Task.objects.all().values('title', 'description', 'status')
        with open('tasks.json', 'w') as file:
            json.dump(list(tasks), file)
        return redirect('task_list')

    @staticmethod
    def load_tasks(request):
        with open('tasks.json', 'r') as file:
            tasks_data = json.load(file)
        for task_data in tasks_data:
            Task.objects.create(**task_data)
        return redirect('task_list')
