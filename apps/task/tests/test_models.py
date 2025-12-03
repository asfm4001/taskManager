from django.test import TestCase

# Create your tests here.
from apps.task.models import Category, Tag, Task
from django.contrib.auth.models import User

def quickCreateCategory(name):
    return Category.objects.create(name=name)

def quickCreateTag(name):
    return Tag.objects.create(name=name)

def quickCreateUser(username):
    return User.objects.create(username=username)

class CategoryModelTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="分類1")
    
    def test_model_str(self):
        c1 = Category.objects.get(name="分類1")
        self.assertEqual(str(c1), "分類1")

class TagModelTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="標籤1")

    def test_model_str(self):
        t1 = Tag.objects.get(name="標籤1")
        self.assertEqual(str(t1), "標籤1")

class TaskModelTestCase(TestCase):
    def setUp(self):
        u1 = quickCreateUser("使用者1")
        c1 = quickCreateCategory("分類1")
        task1 = Task.objects.create(title="任務1",
                                    category=c1,
                                    owner=u1)
        t1 = quickCreateTag("標籤1")
        task1.tags.add(t1)

    def test_model_str(self):
        STATUS_CHOICES = Task.get_status_choices()
        task1 = Task.objects.get(title="任務1")
        self.assertEqual(str(task1), "任務1")
        self.assertEqual(task1.status, "Pending")
        self.assertEqual(task1.get_status_display(), "待處理")

    def test_model_relation(self):
        task1 = Task.objects.get(title="任務1")
        c1 = Category.objects.get(name='分類1')
        t1 = Tag.objects.get(name="標籤1")
        self.assertEqual(task1.category, c1)
        self.assertIn(t1, task1.tags.all())