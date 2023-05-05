from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from desi_mart.models import Category, Product, Order, Customer, Cart, LineItem
from desi_mart.forms import SignUpForm
from django.contrib.auth.models import User


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
    user = request.user
    if user.is_authenticated:
        customer = get_object_or_404(Customer, user_id=user.id)
        order = Order.objects.create(customer=customer)
        order.refresh_from_db()
        for item in basket:
            product_item = get_object_or_404(Product, id=item['product_id'])
            cart = Cart.objects.create(product = product_item, quantity=item['quantity'])
            cart.refresh_from_db()
            line_item = LineItem.objects.create(quantity=item['quantity'], product=product_item, cart=cart,  order = order)
            line_item.refresh_from_db()

    basket.clear()
    request.session['deleted'] = 'thanks for your purchase'
    return render(request,'desi_mart/orderplaced.html')


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'desi_mart/orders_list.html', {'orders' : orders})

def myorders(request,id):
    customer = get_object_or_404(Customer, user_id=id)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'desi_mart/orders_list.html', {'orders' : orders})



def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    customer = order.customer
    user = get_object_or_404(User, id=customer.pk)
    line_items = LineItem.objects.filter(order_id=order.id)
    return render(request, 'desi_mart/order_detail.html', {'order' : order, 'user': user, 'line_items': line_items})


@login_required
def dashboard(request):
    user = request.user
    if user.is_authenticated & user.is_staff:
        dataset = [];
        for x in range(0,14):
            num = random.randrange(10,100)
            dataset.append(num)
        return render(request, 'desi_mart/dashboard.html',{'dataset': dataset})
    else:
        return redirect('desi_mart:login')


