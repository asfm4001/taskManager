from django import forms
from apps.task.models import Category, Tag

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
                "name": 'Create a new category: ',
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        labels = {
                "name": 'Create a new Tag: ',
        }