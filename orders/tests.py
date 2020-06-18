
from django.test import TestCase   # import the extension of unittest framework
from .models import *
from django.utils import timezone
from .database import *


class OrdersTestCase(TestCase):

    USER = 'admin'

    def setUp(self):
        # a function built-in to unittest/django framework that runs before any individual test

        admin = User.objects.create_user(
            username=self.USER,
            email='admin@admin.org',
            password=self.USER,
            first_name=self.USER,
            last_name=self.USER
        )

        # create menu sections
        regular_pizza = MenuSection.objects.create(name="Regular Pizza")
        subs = MenuSection.objects.create(name="Subs")

        # create some toppings
        pepperoni = Topping.objects.create(type="Pepperoni")
        sausage = Topping.objects.create(type="Sausage")
        mushrooms = Topping.objects.create(type="Mushrooms")
        extra_cheese = Topping.objects.create(type="Extra Cheese")

        # create some sizes
        small = Size.objects.create(value="Small")
        large = Size.objects.create(value="Large")

        # CREATE ITEMS

        # -- 1 Topping Pizza-- #
        item = Item.objects.create(name="Cheese Pizza - 1 Topping")

        price_small = Price.objects.create(item=item, size=small, base_price=13.20)
        price_large = Price.objects.create(item=item, size=large, base_price=19.45)

        # Create Menu Item
        pizza = MenuItem.objects.create(
            category=regular_pizza,
            item=item,
            number_of_possible_toppings=2
        )
        pizza.available_sizes.add(small, large)
        pizza.prices.add(price_small, price_large)
        pizza.available_topping_options.add(pepperoni, sausage)

        # Create Customer Item
        customer_item1 = CustomerItem.objects.create(
            user=admin,
            category=regular_pizza,
            item=pizza,
            size=large,
            price=13.20
        )
        customer_item1.toppings.add(pepperoni, mushrooms)

        # -- Italian Sub-- #
        item = Item.objects.create(name="Italian Sub")

        price_small = Price.objects.create(item=item, size=small, base_price=6.50)
        price_large = Price.objects.create(item=item, size=large, base_price=7.95)

        # Create Menu Item
        italian_sub = MenuItem.objects.create(
            category=subs,
            item=item,
            number_of_possible_toppings=1,
            price_per_additional_topping=0.50
        )
        italian_sub.available_sizes.add(small, large)
        italian_sub.prices.add(price_small, price_large)
        italian_sub.available_topping_options.add(extra_cheese)

        # Create Customer Item
        customer_item2 = CustomerItem.objects.create(
            user=admin,
            category=subs,
            item=italian_sub,
            size=large,
            price=8.45
        )
        customer_item2.toppings.add(extra_cheese)

    def test_menu_item_count(self):
        a = MenuItem.objects.all()

        result = len(a)
        expected = 2
        self.assertEqual(result, expected)

    def test_topping_count(self):
        a = Topping.objects.all()

        result = len(a)
        expected = 4
        self.assertEqual(result, expected)

    def test_calculate_total_cost(self):
        menu_items = CustomerItem.objects.all()

        result = float(calculate_total_cost(menu_items))
        expected = 21.65
        self.assertEqual(result, expected)

    def test_calculate_customer_item_price(self):

        result = calculate_customer_item_price(
            category=MenuSection.objects.get(name='Subs'),
            item_name=MenuItem.objects.filter(category__name='Subs').filter(item__name='Italian Sub').first(),
            size=Size.objects.get(value='Small'),
            toppings=["1", "2"]
        )
        expected = 7.50
        self.assertEqual(result, expected)

    def test_user_has_open_cart_false(self):
        result = user_has_an_open_cart(self.USER)
        expected = False
        self.assertEqual(result, expected)

    def test_user_has_open_cart_true(self):

        order = Order.objects.create(
            user=User.objects.get(username=self.USER),
            cart_created=timezone.now()
        )
        result = user_has_an_open_cart(self.USER)
        expected = True
        self.assertEqual(result, expected)

    def test_create_new_customer_item(self):

        customer_item = create_new_customer_item(
            username=self.USER,
            category='Subs',
            item_name='Italian Sub',
            size='Small',
            toppings=['Pepperoni']
        )

        result = len(CustomerItem.objects.filter(user__username=self.USER).filter(size__value="Small"))
        expected = 1
        self.assertEqual(result, expected)

    def test_add_item_to_customer_cart(self):

        customer_item = CustomerItem.objects.first()
        add_item_to_customer_cart(self.USER, customer_item)

        result = len(Order.objects.filter(user__username=self.USER))
        expected = 1
        self.assertEqual(result, expected)

    def test_place_order(self):

        # create an order.
        customer_item = CustomerItem.objects.first()
        add_item_to_customer_cart(self.USER, customer_item)
        place_order(self.USER)

        in_progress = len(Order.objects.filter(status='progress'))
        in_cart = len(Order.objects.filter(status='cart'))

        result = (in_progress, in_cart)
        expected = (1, 0)
        self.assertEqual(result, expected)
