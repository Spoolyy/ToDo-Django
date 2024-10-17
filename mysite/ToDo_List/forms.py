from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "content",
            "notes",
            "pub_date",
            "due_date",
            "priority",
            "category",
            "is_completed",
        ]