from django.urls import path
from . import views

app_name = "todo-list"

urlpatterns = [
    path("task/", views.index, name="index"),
    path("task/createnew", views.create, name="create")
]
