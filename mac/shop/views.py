from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil

def index(request):
    products = product.objects.all()
    # print(products)

    # params = {'nSlides':nSlides,'product':products,'range':range(1,nSlides)}
    # allProds=[[products,range(1,nSlides),nSlides],
    #           [products, range(1, nSlides), nSlides]
    #           ]
    allProds = []
    catProds = product.objects.values('category','id')
    cats={item['category'] for item in catProds}
    for cat in cats:
        prod = product.objects.filter(category = cat)
        n = len(products)
        nSlides = n // 4 + ceil(n / 4 - (n // 4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')

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

