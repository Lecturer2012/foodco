from django.shortcuts import render
from django.http import HttpResponse
from.models import item

# Create your views here.
def home(request):
    items = item.objects.all()
    return render(request, "home/home.html", {'items': items})

def menu(request):
    return render(request, "home/menu.html")

def about(request):
    return render(request, "home/about.html")

def book(request):
    return render(request, "home/book.html")
