from django.urls import path
from apps.api.views import *

app_name = "api"

urlpatterns = [
    path('v1/task/', TaskViewSets.as_view(), name="v1_task_sets"),
    path('v1/category/', CategoryViewSets.as_view(), name="v1_category_sets"),
    path('v1/tag/', TagViewSets.as_view(), name="v1_tag_sets"),
]
