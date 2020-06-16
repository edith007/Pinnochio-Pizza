from django.db import models


class MenuSection(models.Model):
    section = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.section}"


class Topping(models.Model):
    type = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.type}"


class Item(models.Model):
    category = models.ForeignKey(MenuSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    size = models.CharField(max_length=60, blank=True)
    number_of_toppings = models.IntegerField(default=0)
    toppings = models.ManyToManyField(Topping, blank=True, related_name="custom_items")
    price = models.DecimalField(max_digits=10, decimal_places=2)  # support USD$

    def __str__(self):
        return f"{self.category} - {self.name}  " \
               f"(size: {self.size}, # toppings: {self.number_of_toppings}, price: ${self.price})"


class Order(models.Model):
    STATUSES = (
        ('cart', 'Cart'),
        ('progress', 'In Progress'),
        ('oiw', 'On it\'s Way')
    )

    user = models.CharField(max_length=60)
    date_placed = models.DateField()
    time_placed = models.TimeField()
    items = models.ManyToManyField(Item, related_name="cart")
    status = models.CharField(max_length=10, choices=STATUSES, default='cart')

    def __str__(self):
        return f"Order ({self.date_placed} {self.time_placed})"
