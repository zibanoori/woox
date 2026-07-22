from django.shortcuts import render
from .models import Core


def index(request):
    base_details = Core.objects.all().first()
    context = {
        "core": base_details
    }
    return render(request,"index.html")
