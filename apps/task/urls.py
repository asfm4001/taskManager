from django.urls import path
from apps.task.views import *

app_name = "task"

urlpatterns = [
    path('category/', CategoryListView.as_view(), name="category_list"),
    # path('category/<int:pk>', CategoryDetailView.as_view(), name="category_detail"),
    path('tag/', TagListView.as_view(), name="tag_list"),
    path('', TaskListView.as_view(), name="task_list"),
    path('<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path('create/', TaskCreateView.as_view(), name="task_create"),
    path('create/category/', CategoryCreateView.as_view(), name="category_create"),
    path('create/tag/', TagCreateView.as_view(), name="tag_create"),
]
