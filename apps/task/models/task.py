from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ("Pending", "待處理"),
        ("In progress", "處理中"),
        ("Done", "完成"),
        ("Delete", "刪除"),
    ]
    title = models.CharField(max_length=20)
    # 原import <modelName>, 更改成使用字串, 避免循環依賴
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="task")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="tasks")
    tags = models.ManyToManyField("Tag", related_name='tasks', blank=True) # null = True(default)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @classmethod
    def get_status_choices(self):
        return self.STATUS_CHOICES