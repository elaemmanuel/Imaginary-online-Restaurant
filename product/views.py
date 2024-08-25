from django.shortcuts import render
from .models import Product
from django.http import HttpResponseNotFound

# Create your views here.

def about_us(request):
    return render(request,'product/about_us.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'product/products.html', {'products': products})


def contact_us(request):
    return render(request, 'product/contact_us.html')

def product_page(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product/product_page.html', {'product': product} )
