from django import forms
from to_do.models import Task, Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "complited", "tags"]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }
