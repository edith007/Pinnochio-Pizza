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
    category = models.ForeignKey(MenuSection, on_delete=models.CASCADE)
    name = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # support USD$

    def __str__(self):
        return f"{self.category} - {self.name} (size: {self.size}, price: ${self.price})"


class Order(models.Model):

    STATUSES = (
        ('cart', 'Cart'),
        ('progress', 'In Progress'),
        ('oiw', 'On it\'s Way')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    datetime_placed = models.DateTimeField()
    datetime_fullfilled = models.DateTimeField(default=None, blank=True)
    items = models.ManyToManyField(CustomerItem, related_name="cart")
    status = models.CharField(max_length=10, choices=STATUSES, default='cart')

    def __str__(self):
        return f"Order (User: {self.user}, Time: {self.datetime_placed})"
