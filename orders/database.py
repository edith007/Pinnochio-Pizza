from .models import *
from .errors import *
from django.utils import timezone


def username_already_exists(username):
    return User.objects.filter(username=username).exists()


def create_new_user(username, email, password, first_name, last_name):
    User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )


def get_items_by_category(category):
    return MenuItem.objects.filter(category__name=category)


def get_menu_catgories():
    return MenuSection.objects.all()


def get_user_by_username(username):
    return User.objects.get(username=username)


def user_is_superuser(username):
    return True if User.objects.filter(is_superuser=True).filter(username=username) else False


def get_menu_section_by_name(section_name):
    return MenuSection.objects.get(name=section_name)


def get_menu_size_by_value(size):
    return Size.objects.get(value=size)


def get_menu_item_by_attributes(category, item_name):
    print(f"{category}...{item_name}")
    item = MenuItem.objects.filter(category__name=category).filter(item__name=item_name)
    if len(item) > 1:
        raise ItemToCartException("Multiple items distinct on section + item for submitted item. Resolve duplicate.")
    return item.first()


def user_has_an_open_cart(username):
    return True if Order.objects.filter(user__username=username).filter(status='cart') else False


def get_active_cart(username):
    return Order.objects.filter(user__username=username).filter(status="cart").first()


def get_items_in_cart(username):
    order = Order.objects.filter(user__username=username).filter(status="cart").first()
    return order.items.all() if order else None


def calculate_customer_item_price(category, item_name, size, toppings):

    item = get_menu_item_by_attributes(category, item_name)
    added_price = item.price_per_additional_topping * len(toppings)
    base_price = Price.objects.filter(item__name=item.item.name).filter(size__value=size).first().base_price

    return added_price + base_price


def calculate_total_cost(customer_items):
    """
    Calculates the current total cost of all items in cart (excluding taxes).
    :param customer_items: A QuerySet (list) containing CustomerItem() objects
    :return: integer representing total cost
    """

    total_cost = 0
    for customer_item in customer_items:
        total_cost += customer_item.price

    return total_cost


def create_new_customer_item(username, category, item_name, size, toppings):

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

    if user_has_an_open_cart(username):
        cart = Order.objects.filter(user__username=username).filter(status="cart").first()
    else:
        cart = Order.objects.create(
            user=get_user_by_username(username),
            cart_created=timezone.now()
        )
    cart.items.add(customer_item)
    cart.final_cost = calculate_total_cost(cart.items.all())
    cart.save()


def place_order(username):

    cart = get_active_cart(username)
    cart.status = 'progress'
    cart.order_placed = timezone.now()
    cart.final_cost = calculate_total_cost(cart.items.all())
    cart.save()


def get_all_orders():
    return Order.objects.all()
