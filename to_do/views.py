from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from to_do.models import Task, Tag
from to_do.forms import TagForm, TaskForm


def index(request):
    tasks = Task.objects.all().order_by("-datetime", "complited")
    return render(request, "to_do/index.html", {"tasks": tasks})


class TagListView(generic.ListView):
    model = Task
    template_name = "to_do/tag_list.html"
    context_object_name = "tegs"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "to_do/tag_create.html"
    success_url = reverse_lazy("to_do:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "to_do/tag_update.html"
    success_url = reverse_lazy("to_do:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "to_do/tag_confirm_delete.html"
    success_url = reverse_lazy("to_do:tag_list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do/task_create.html"
    success_url = reverse_lazy("to_do:index")
