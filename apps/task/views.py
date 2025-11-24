from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from apps.task.models import Category, Tag, Task
from apps.task.forms import CategoryForm, TagForm
# Create your views here.
class CategoryListView(generic.ListView):
    model = Category

class CategoryListCreateView(FormMixin, generic.ListView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('task:category_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class CategoryCreateView(generic.CreateView):
    model = Category
    fields = ['name']

class TagListView(FormMixin, generic.ListView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('task:tag_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class TaskListView(generic.ListView):
    model = Task

class TagCreateView(generic.CreateView):
    model = Tag
    fields = ['name']

class TaskDetailView(generic.DetailView):
    model = Task
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status_choices"] = Task.get_status_choices()
        return context

class TaskCreateView(generic.CreateView):
    model = Task
    fields = ['title', 'category', 'tags', 'status']
    success_url = reverse_lazy("task:task_list")
    def form_valid(self, form):
        # 將當前使用者設為 owner
        form.instance.owner = self.request.user
        return super().form_valid(form)