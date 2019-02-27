from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("About page")

def contact(request):
    return HttpResponse("contact page")

def tracker(request):
    return HttpResponse("tracker page")

def search(request):
    return HttpResponse("search page")

def productView(request):
    return HttpResponse("productView page")

def checkout(request):
    return HttpResponse("checkout page")

