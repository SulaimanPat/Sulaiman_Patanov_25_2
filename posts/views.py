from django.shortcuts import HttpResponse, redirect
from datetime import datetime

# Create your views here.

def hello_view(request):
    if request.method=="GET":
        return HttpResponse("Hello! Its my first project)")

def now_date(request):
    current_datetime=datetime.now()
    if request.method=="GET":
        return HttpResponse(current_datetime)

def goodby(request):
    if request.method=="GET":
        return HttpResponse("Goodby user!")

def youtube_view(request):
    if request.method=="GET":
        return redirect("https://www.youtube.com/")
