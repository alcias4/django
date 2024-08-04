from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
# Create your views here.


def projects(resquest):
    resp = list(Project.objects.values())
    return JsonResponse(resp, safe=False)


def add_projects(request):
    if request.method == "POST":
        print(request.POST)
        return JsonResponse({"mensaje": "hola"})


def task(resquest, id):
    task = get_object_or_404(Task, id= id)
    return HttpResponse(task.title)