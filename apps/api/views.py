from django.shortcuts import render
from apps.task.models import *
from apps.api.serializers import *
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

# List
class TaskViewSets(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryViewSets(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSets(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer