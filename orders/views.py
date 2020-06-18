from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Order, Topping, CustomerItem, MenuItem, MenuSection
from .database import *


def index(request):

    if not request.user.is_authenticated:
        return render(request, 'orders/login.html', {'message': None})

    # get the information required.
    menu_objects = dict()
    for category in get_menu_catgories():
        menu_objects[category.name] = get_items_by_category(category.name)

    return render(request, 'orders/index.html', {'menu': menu_objects})


def login_view(request):

    print(f"Attempting to authenticate: {request.POST['username']} {request.POST['password']}")
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )

    if user:  # authenticated
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'orders/login.html', {'login_message': 'Authentication failed.'})


def register(request):
    return render(request, 'orders/register.html', {'registration_message': 'Please provide your information.'})


def registration_attempt(request):

    submitted_username = request.POST['username']

    if username_already_exists(submitted_username):
        return render(request, 'orders/register.html', {'registration_message': 'Username already exists.'})

    create_new_user(
        username=request.POST['username'],
        email=request.POST['email'],
        password=request.POST['password'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name']
    )

    print(f"Created new user ({submitted_username} @ {request.POST['password']})")
    return render(request, 'orders/login.html', {'login_message': 'Successful registration! Please login.'})


def add_item_to_cart(request):

    username = request.user.username
    category = request.POST['item'].split("_")[0]
    item_name = request.POST['item'].split("_")[1]
    size = request.POST['size']
    toppings = request.POST.getlist('toppings')

    print(f"Adding new item to {username}'s cart: {category}, {item_name} (Size: {size}, Toppings: {toppings})")
    customer_item = create_new_customer_item(
        username=username,
        category=category,
        item_name=item_name,
        size=size,
        toppings=toppings
    )
    add_item_to_customer_cart(username, customer_item)

    return HttpResponseRedirect(reverse('index'))


def view_cart(request):

    cart_items = get_items_in_cart_by_user(request.user.username)
    context = {
        'items': cart_items,
        'total_cost': calculate_total_cost(cart_items),
        'message': 'Are you ready to checkout?'
    }
    return render(request, 'orders/cart.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'orders/login.html', {'login_message': 'Logged out.'})
