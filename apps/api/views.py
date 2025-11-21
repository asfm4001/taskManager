from django.shortcuts import render
from apps.task.models import *
from apps.api.serializers import *
from rest_framework import generics

# List
class TaskViewSets(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CategoryViewSets(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSets(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer