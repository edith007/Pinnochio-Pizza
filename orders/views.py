from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .database import *
from django.core.mail import send_mail
from django.conf import settings
from random import randint


def index(request):

    if not request.user.is_authenticated:
        return render(request, 'orders/login.html', {'message': None})

    # get the menu items from the database
    menu_objects = dict()
    for category in get_menu_catgories():
        menu_objects[category.name] = get_items_by_category(category.name)

    # get any items currently in the user's cart
    cart_items = get_items_in_cart(request.user.username)

    context = {
        'is_admin': user_is_superuser(request.user.username),
        'menu': menu_objects,
        'items_in_cart': len(cart_items) if cart_items else 0
    }
    return render(request, 'orders/index.html', context)


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


def view_all_orders(request):

    cart_items = get_items_in_cart(request.user.username)
    context = {
        'is_admin': user_is_superuser(request.user.username),
        'items_in_cart': len(get_items_in_cart(request.user.username)) if cart_items else 0,
        'orders': get_all_orders()
    }
    return render(request, 'orders/all_orders.html', context)


def view_cart(request):

    cart_items = get_items_in_cart(request.user.username)
    context = {
        'is_admin': user_is_superuser(request.user.username),
        'items': cart_items,
        'total_cost': calculate_total_cost(cart_items) if cart_items else None,
        'items_in_cart': len(get_items_in_cart(request.user.username)) if cart_items else 0,
        'order_placed': False,
    }
    return render(request, 'orders/cart.html', context)


def order_items_in_cart(request):

    place_order(request.user.username)
    send_confirmation_email(request.POST['receipt_email'])

    context = {
        'user': request.user.username,
        'is_admin': user_is_superuser(request.user.username),
        'order_placed': True,
    }
    return render(request, 'orders/cart.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'orders/login.html', {'login_message': 'Logged out.'})


def send_confirmation_email(user_email):

    print("Attempting to send email!")

    subject = "Pinnochio’s Pizza & Subs Order Confirmation"
    message = f""" Hello there!
                   \nThis is an automated message confirming your recently placed order with us (order #{randint(100, 999)}).
                   \nThank you for ordering from us! Come back again soon!
                   \n Stay saucy,
                   \n Pinnochio's Email Bot
               """

    sender = settings.EMAIL_HOST_USER
    recipient_list = [user_email, ]

    send_mail(
        subject=subject,
        message=message,
        from_email=sender,
        recipient_list=recipient_list,
        fail_silently=False
    )
