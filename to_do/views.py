from django.shortcuts import render
from django.views import generic

from to_do.models import Task


def index(request):
    tasks = Task.objects.all().order_by("-datetime", "complited")
    return render(request, "to_do/index.html", {"tasks": tasks})

