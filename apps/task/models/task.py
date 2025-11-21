from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=20)
    # 原import <modelName>, 更改成使用字串, 避免循環依賴
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="task")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="task")
    tags = models.ManyToManyField("Tag", related_name='tasks', blank=True) # null = True(default)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    