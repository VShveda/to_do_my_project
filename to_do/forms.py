from django import forms
from to_do.models import Task, Tag


class TagUpdateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
