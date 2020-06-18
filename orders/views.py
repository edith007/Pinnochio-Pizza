from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .database import *
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    """
    The main entry point for the application, checking if user is signed in,
    and if so, bringing them to the main 'Menu' page of the application.
    """

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
    """
    Called on when a user attempts to login to the website, attempt to log user in
    and, if successful, go back to index() route. Otherwise, ask the user to try again.
    """

    print(f"Attempting to authenticate: {request.POST['username']} {request.POST['password']}")
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )

    if user:  # user is authenticated, so bring them to the Menu
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'orders/login.html', {'login_message': 'Authentication failed.'})


def register(request):
    """Route called on when a user attempts to newly register for an account with the application."""
    return render(request, 'orders/register.html', {'registration_message': 'Please provide your information.'})


def registration_attempt(request):
    """
    Route called when user submits their registration information. If the username is
    already taken, prompt user again. If not, create the new user and return them to the
    login page to try their login with their newly created credentials.
    """

    submitted_username = request.POST['username']

    if username_already_exists(submitted_username):
        return render(request, 'orders/register.html', {'registration_message': 'Username already exists.'})

    # if user doesn't already exist, then create it.
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
    """
    Route called on when user attempts to add an item to their cart from the main menu page.
    Adds a new CustomerItem() to the database and adds the CustomerItem() to the customers 'open' cart.
    """

    # get info from request
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

    return HttpResponseRedirect(reverse('index'))  # bring user back to main Menu Page again


def view_all_orders(request):
    """
    Called on only when a user is a 'superuser' who clicks on the 'View all Orders' button,
    surfaces ALL orders in the database in the UI.
    """

    cart_items = get_items_in_cart(request.user.username)
    context = {
        'is_admin': user_is_superuser(request.user.username),
        'items_in_cart': len(get_items_in_cart(request.user.username)) if cart_items else 0,
        'orders': get_all_orders()
    }
    return render(request, 'orders/all_orders.html', context)


def view_cart(request):
    """
    Route called on when a user requests to see their cart by clicking on the cart icon, gets
    all items currently in the user's active, open cart.
    """

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
    """
    Route called on when a user clicks on the 'Order Food' button in the UI in order to
    place the order (i.e., update the Order() object in the database) and send the user a
    confirmation email.
    """

    # if the user hasn't provided an email, don't do anything
    if request.POST['receipt_email'] is None:
        return None

    order = place_order(request.user.username)
    send_confirmation_email(request.POST['receipt_email'], order)

    # Tell the user that the order placement was successful
    context = {
        'user': request.user.username,
        'is_admin': user_is_superuser(request.user.username),
        'order_placed': True,
    }
    return render(request, 'orders/cart.html', context)


def logout_view(request):
    """
    Called to log user out of the main program
    """
    logout(request)
    return render(request, 'orders/login.html', {'login_message': 'Logged out.'})


def send_confirmation_email(user_email, order):
    """
    Sends the user an automated confirmation email about their order, once it is placed.

    :param user_email: String representing user's email (i.e., 'abcd1234@gmail.com').
    :param order: Order() database object
    """

    subject = "Pinnochio’s Pizza & Subs Order Confirmation"
    message = f""" Hello there! 
                   \nThis is an automated message confirming your recently placed order (order #{order.id}). 
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

