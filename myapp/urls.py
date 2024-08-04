from django.urls import path
from . import views

urlpatterns  = [
    path("projects/", views.projects),
    path("task/<int:id>", views.task),
    path("add_project/", views.add_projects)
]