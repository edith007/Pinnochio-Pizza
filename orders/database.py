from .models import Order, Topping, Item, MenuSection

class MenuDB:

    def distinct_regular_pizzas(self):
        return Item.objects.filter(category_section="Regular_pizza").exclude(size__value="Large")

    def distinct_sicilian_pizzas(self):
        return Item.objects.filter(category_section="Sicilian Pizza").exclude(size__value="Large")

    def distinct_pastas(self):
        return Item.objects.filter(category_section="Pasta")

    def distinct_subs(self):
        return Item.objects.filter(category_section="Subs").exclude(size__value="Large")

    def distinct_salads(self):
        return Item.objects.filter(category_section="Salads")

    def distinct_platters(self):
        return Item.objects.filter(category_section="Dinner Platters").exclude(size__value="Large")

    def get_toppings(self):
        return Topping.objects.all()
