from django.shortcuts import render

from to_do.models import Task


def index(request):
    tasks = Task.objects.all().order_by("-datetime", "complited")
    return render(request, "index.html", {"tasks": tasks})
