from django.shortcuts import render
from .models import Core


def index(request):
    base_details = Core.objects.all().first()
    context = {
        "Core": base_details
    }
    return render(request,"index.html")
