from .models import Order, Topping, CustomerItem, MenuItem, MenuSection


class MenuDB:

    def distinct_regular_pizzas(self):
        return MenuItem.objects.filter(category__section="Regular Pizza").exclude(size__value="Large")

    def distinct_sicilian_pizzas(self):
        return MenuItem.objects.filter(category__section="Sicilian Pizza").exclude(size__value="Large")

    def distinct_pastas(self):
        return MenuItem.objects.filter(category__section="Pasta")

    def distinct_subs(self):
        return MenuItem.objects.filter(category__section="Subs").exclude(size__value="Large")

    def distinct_salads(self):
        return MenuItem.objects.filter(category__section="Salads")

    def distinct_platters(self):
        return MenuItem.objects.filter(category__section="Dinner Platters").exclude(size__value="Large")

    def get_toppings(self):
        return Topping.objects.all()
