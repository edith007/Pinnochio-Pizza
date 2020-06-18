from django.db import models
from django.contrib.auth.models import User


class MenuSection(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name}"


class Size(models.Model):
    value = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.value}"


class Topping(models.Model):
    type = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.type}"


class Item(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name}"


class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item} ({self.size}): ${self.base_price}"


class MenuItem(models.Model):
    category = models.ForeignKey(MenuSection, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    available_sizes = models.ManyToManyField(Size, default='One-Size')
    number_of_possible_toppings = models.IntegerField(default=0,  blank=True)
    available_topping_options = models.ManyToManyField(Topping, blank=True, related_name="selected_toppings")
    price_per_additional_topping = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    prices = models.ManyToManyField(Price)

    def __str__(self):
        if self.category in ["Regular Pizza", "Sicilian Pizza"]:
            return f"{self.item} ({self.number_of_possible_toppings} toppings)"
        else:
            return f"{self.item}"


class CustomerItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    category = models.ForeignKey(MenuSection, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # support USD$

    def __str__(self):
        return f"{self.item}, price: ${self.price}, belonging to {self.user}"


class Order(models.Model):

    CART = 'cart'
    PROGRESS = 'progress'
    TRANSIT = 'transit'
    COMPLETE = 'complete'

    STATUSES = (
        (CART, 'In Cart'),
        (PROGRESS, 'In Progress'),
        (TRANSIT, 'On it\'s Way'),
        (COMPLETE, 'Complete')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    cart_created = models.DateTimeField()
    order_placed = models.DateTimeField(null=True)
    order_fullfilled = models.DateTimeField(null=True)
    items = models.ManyToManyField(CustomerItem, related_name="cart")
    status = models.CharField(max_length=15, choices=STATUSES, default=CART)

    def __str__(self):
        if self.order_fullfilled:
            return f"Order {self.status} (User: {self.user}, Order Fullfilled: {self.order_fullfilled})"
        if self.order_placed:
            return f"Order {self.status} (User: {self.user}, Order Placed: {self.order_placed})"
        else:
            return f"Order {self.status} (User: {self.user}, Cart Created: {self.cart_created})"
