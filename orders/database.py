"""
Contains function necessary for interacting the with the Pizza database.
"""
from .models import *
from .errors import *
from django.utils import timezone


def username_already_exists(username):
    """
    Determines if username is already taken in the database.

    :param username: A string representing the proposed new username
    :return: boolean representing existence of the the username already
    """
    return User.objects.filter(username=username).exists()


def create_new_user(username, email, password, first_name, last_name):
    """
    Adds a new user to the database.

    :param username: String representing username, submitted by user in UI
    :param email: String representing email, submitted by user in UI
    :param password: String representing password, submitted by user in UI
    :param first_name: String representing first_name, submitted by user in UI
    :param last_name: String representing last_name, submitted by user in UI
    :return:
    """
    User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )


def get_items_by_category(category):
    """
    Get's all existing database MenuItem() objects for a provided category.

    :param category: String representing one of the Menu Section categories
    :return QuerySet() of MenuItem() objects
    """
    return MenuItem.objects.filter(category__name=category)


def get_menu_catgories():
    """
    Get's all MenuSection() objects currently in database.

    :return: QuerySet() (list) of MenuSection() items
    """
    return MenuSection.objects.all()


def get_user_by_username(username):
    """
    Get's User() object currently in database for a provided username.

    :param username: String representing username
    :return: Single User() object
    """
    return User.objects.get(username=username)


def user_is_superuser(username):
    """
    Determines if a given user (identified by username) is a superuser.

    :param username: String representing username
    :return: boolean representing 'if' user is superuser
    """
    return True if User.objects.filter(is_superuser=True).filter(username=username) else False


def get_menu_section_by_name(section_name):
    """
    Find MenuSection() object by it's section name. Note MenuSection() must already exist.

    :param section_name:  String representing name of section (e.g., 'Pasta')
    :return: MenuSection() object
    """
    return MenuSection.objects.get(name=section_name)


def get_menu_size_by_value(size):
    """
    Get Size() object existing in database by size. Note Size() must already exist.

    :param size:  String representing size (e.g., 'Small', 'Large', 'One_Size')
    :return: Size() object
    """
    return Size.objects.get(value=size)


def get_menu_item_by_attributes(category, item_name):
    """
    Find the MenuItem() object in database by it's category and name.

    :param category:  String representing category (e.g., 'Subs')
    :param item_name:  String representing item name (e.g., 'Meatball Sub')
    :return: matching MenuItem() object
    :raises ItemToCartException if there are multiple objects with the same category-item combination.
    """
    item = MenuItem.objects.filter(category__name=category).filter(item__name=item_name)
    if len(item) > 1:
        raise ItemToCartException("Multiple items distinct on section + item for submitted item. Resolve duplicate.")
    return item.first()


def user_has_an_open_cart(username):
    """
    Determine if a given user has an "open" cart (i.e., a cart that hasn't be officially purchased yet).

    :param username: String representing username
    :return: boolean, if open cart
    """
    return True if Order.objects.filter(user__username=username).filter(status='cart') else False


def get_active_cart(username):
    """
    Finds the active 'open' cart (Order() without a 'order_placed' date) by user.

    :param username:  String representing username
    :return: open Order() object for user; if no Order() found, returns None.
    """
    return Order.objects.filter(user__username=username).filter(status="cart").first()


def get_items_in_cart(username):
    """
    Finds all MenuItems() in the 'open' cart (Order() without a 'order_placed' date) by user.
    :param username: String representing username

    :return: QuerySet() of MenuItem() objects if an open cart exists, else None
    """
    order = Order.objects.filter(user__username=username).filter(status="cart").first()
    return order.items.all() if order else None


def calculate_customer_item_price(category, item_name, size, toppings):
    """
    Calculates the price of a given CustomerItem(), based on its base price and additional
    cost due to toppings (if applicable).

    :param category:  String representing category (i.e., 'Subs')
    :param item_name:  String representing item name (i.e., 'Meatball Sub')
    :param size:  String representing size (i.e., 'Small')
    :param toppings:  list() representing all toppings selected by user
    :return:  price of item, as float
    """

    item = get_menu_item_by_attributes(category, item_name)
    added_price = item.price_per_additional_topping * len(toppings)
    base_price = Price.objects.filter(item__name=item.item.name).filter(size__value=size).first().base_price

    return added_price + base_price


def calculate_total_cost(customer_items):
    """
    Calculates the current total cost of all items in cart (excluding taxes).
    :param customer_items: A QuerySet (list) containing CustomerItem() objects
    :return: total cost, as float
    """

    total_cost = 0
    for customer_item in customer_items:
        total_cost += customer_item.price

    return total_cost


def create_new_customer_item(username, category, item_name, size, toppings):
    """
    Creates a new CustomerItem() object in the database, called when a user adds an item
    to their cart in the UI.

    :param username: String representing username (i.e, 'admin')
    :param category: String representing category (i.e., 'Subs')
    :param item_name: String representing item name (i.e., 'Meatball Sub')
    :param size: String representing size (i.e., 'Small')
    :param toppings: list() representing all toppings selected by user
    :return: newly created CustomerItem() database object
    """

    customer_item = CustomerItem.objects.create(
        user=get_user_by_username(username),
        category=get_menu_section_by_name(category),
        item=get_menu_item_by_attributes(category, item_name),
        size=get_menu_size_by_value(size),
        price=calculate_customer_item_price(category=category, item_name=item_name, size=size, toppings=toppings)
    )
    for topping in toppings:
        topping_object = Topping.objects.get(type=topping)
        customer_item.toppings.add(topping_object)

    return customer_item


def add_item_to_customer_cart(username, customer_item):
    """
    Adds a new CustomerItem() to a given user's 'open cart' (i.e., Order() without an
    'order_placed' date).

    :param username: String representing username (i.e, 'admin')
    :param customer_item: CustomerItem() object
    """

    if user_has_an_open_cart(username):
        cart = Order.objects.filter(user__username=username).filter(status="cart").first()
    else:
        cart = Order.objects.create(
            user=get_user_by_username(username),
            cart_created=timezone.now()
        )
    cart.items.add(customer_item)
    cart.total_cost = calculate_total_cost(cart.items.all())
    cart.save()


def place_order(username):
    """
    Called on when user 'checks out' their cart in the UI, method 'places' the order by
    updating corresponding the Order() object in the database to have a new 'status', 'order_placed',
    and 'total_cost' field.

    :param username: String representing username (i.e, 'admin')
    :return order: The Order() object updated.
    """

    cart = get_active_cart(username)
    cart.status = 'progress'
    cart.order_placed = timezone.now()
    cart.total_cost = calculate_total_cost(cart.items.all())
    cart.save()

    return cart


def get_all_orders():
    """
    Get all Order() objects; serves the superuser UI regarding all orders.
    :return: QuerySet() of Order() objects.
    """
    return Order.objects.all()


