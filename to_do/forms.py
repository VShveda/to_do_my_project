from django import forms
from .models import Task, Tag


class TagUpdateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
