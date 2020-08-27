from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
    "msg": "Hello World!",
    "name": "Khalid",
    "task": "02"
    }

    return render(request, "home.html", context)
