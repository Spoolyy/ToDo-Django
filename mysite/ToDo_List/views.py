from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.utils import timezone
from datetime import timedelta

def index(request):
    tasks = Task.objects.all()
    current_time = timezone.now()
    one_day_from_now = current_time + timedelta(days=1)
    return render(request, "index.html", {"tasks":tasks, "current_time":current_time, "one_day_from_now":one_day_from_now})

def create(request):
    if request.method == "POST":
        pass