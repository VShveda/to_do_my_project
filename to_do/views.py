from django.shortcuts import render
from django.views import generic

from to_do.models import Task


def index(request):
    tasks = Task.objects.all().order_by("-datetime", "complited")
    return render(request, "to_do/index.html", {"tasks": tasks})


class TagListView(generic.ListView):
    model = Task
    template_name = "to_do/tag_list.html"
    context_object_name = "tegs"
