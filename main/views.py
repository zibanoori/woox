from django.shortcuts import render
from .models import Core


def index(request):
    return render(request,"index.html")
