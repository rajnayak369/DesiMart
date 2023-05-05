from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from desi_mart.models import Category, Product
from desi_mart.forms import SignUpForm

import random

from desi_mart.views.basket import Basket


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.customer.first_name = form.cleaned_data.get('first_name')
        user.customer.last_name = form.cleaned_data.get('last_name')
        user.customer.address = form.cleaned_data.get('address')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password= password)
        login(request, user)
        return redirect('/')
    return render(request, 'desi_mart/signup.html', {'form': form})

def home(request):
    return render(request,"desi_mart/homepage.html")


def place_order(request):
    basket = Basket(request)
    if request.method == "POST":
        address_data = request.POST.dict()
        first_name = address_data.get("first_name")
        last_name = address_data.get("last_name")
        email = address_data.get("email")
        address = address_data.get("address")
        return render(request, 'desi_mart/checkout.html', {'basket': basket, 'address': address, 'first_name': first_name, 'last_name': last_name, 'email':email})
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'desi_mart/checkout.html', {'basket': basket})
    else:
        return  render(request, 'desi_mart/address_info.html', {'basket': basket})


def order_success(request):
    basket = Basket(request)
    basket.clear()
    request.session['deleted'] = 'thanks for your purchase'
    return render(request,'desi_mart/orderplaced.html')