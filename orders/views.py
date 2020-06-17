from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Order, Topping, CustomerItem, MenuItem, MenuSection
from .database import MenuDB

menu = MenuDB()


def index(request):

    if not request.user.is_authenticated:
        return render(request, 'orders/login.html', {'message': None})

    # get the information required.
    context = {
        'user': request.user,
        'regular_pizzas': menu.distinct_regular_pizzas(),
        'silician_pizzas': menu.distinct_sicilian_pizzas(),
        'subs': menu.distinct_subs(),
        'pastas': menu.distinct_pastas(),
        'salads': menu.distinct_salads(),
        'platters': menu.distinct_platters(),
        'toppings': menu.get_toppings()
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

    if User.objects.filter(username=submitted_username).exists():
        return render(request, 'orders/register.html', {'registration_message': 'Username already exists.'})

    User.objects.create_user(
        username=request.POST['username'],
        email=request.POST['email'],
        password=request.POST['password'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name']
    )

    print(f"Created new user ({submitted_username} @ {request.POST['password']})")
    return render(request, 'orders/login.html', {'login_message': 'Successful registration! Please login.'})


def add_item_to_cart(request):
    return None


def logout_view(request):
    logout(request)
    return render(request, 'orders/login.html', {'login_message': 'Logged out.'})
