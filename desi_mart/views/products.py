from django.shortcuts import get_object_or_404, render

from desi_mart.forms import BasketAddProductForm
from desi_mart.models import Category, Product
import random


def all_products(request):
    products = Product.objects.all()
    return render(request, 'desi_mart/products.html', {'products': products})


def category_products(request, category):
    category_obj = get_object_or_404(Category, name=category)
    products = Product.objects.filter(category=category_obj.id)
    return render(request,"desi_mart/products.html", {'products': products})


def search_products(request):
    search_query = request.GET['query']
    products = Product.objects.filter(title__icontains=search_query)
    return render(request,"desi_mart/products.html", {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    products = Product.objects.filter(category=product.category)
    start = random.randrange(1, len(products))
    if len(products)-start>5:
        end = start+5
    else:
        end = len(products)
    return render(request,"desi_mart/product_detail.html", {'product': product, 'products': products[start:end], 'basket_product_form' :BasketAddProductForm()})