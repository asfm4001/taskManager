from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from apps.task.models import Category, Tag, Task
# Create your views here.
class CategoryListView(generic.ListView):
    model = Category

class CategoryCreateView(generic.CreateView):
    model = Category
    fields = ['name']

class TagListView(generic.ListView):
    model = Tag

class TaskListView(generic.ListView):
    model = Task

class TagCreateView(generic.CreateView):
    model = Tag
    fields = ['name']

class TaskDetailView(generic.DetailView):
    model = Task

class TaskCreateView(generic.CreateView):
    model = Task
    fields = ['title', 'category', 'tags']
    success_url = reverse_lazy("task:task_list")