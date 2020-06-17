"""
Sets up database from scratch, if necessary, to reflect Pinnochio’s Pizza on 06/2020
"""
from orders.models import *


# ------ Add Toppings to Database ------ #

pepperoni = Topping(type="Pepperoni")
sausage = Topping(type="Sausage")
mushrooms = Topping(type="Mushrooms")
onions = Topping(type="Onions")
ham = Topping(type="Ham")
canadian_bacon = Topping(type="Canadian Bacon")
pineapple = Topping(type="Pineapple")
eggplant = Topping(type="Eggplant")
tomato_basil = Topping(type="Tomato & Basil")
green_peppers = Topping(type="Green Peppers")
hamburger = Topping(type="Hamburger")
spinach = Topping(type="Spinach")
artichoke = Topping(type="Artichoke")
buffalo_chicken = Topping(type="Buffalo Chicken")
barbecue_chicken = Topping(type="Barbecue Chicken")
anchovies = Topping(type="Anchovies")
black_olives = Topping(type="Black Olives")
garlic = Topping(type="Fresh Garlic")
zucchini = Topping(type="Zucchini")
extra_cheese = Topping(type="Extra Cheese")

pepperoni.save()
sausage.save()
mushrooms.save()
onions.save()
ham.save()
canadian_bacon.save()
pineapple.save()
eggplant.save()
tomato_basil.save()
green_peppers.save()
hamburger.save()
spinach.save()
artichoke.save()
buffalo_chicken.save()
barbecue_chicken.save()
anchovies.save()
black_olives.save()
garlic.save()
zucchini.save()
extra_cheese.save()   # sub only

# ------ Add Menu Sections to Database ------ #

regular_pizza = MenuSection(section="Regular Pizza")
sicilian_pizza = MenuSection(section="Sicilian Pizza")
subs = MenuSection(section="Subs")
pasta = MenuSection(section="Pasta")
salads = MenuSection(section="Salads")
platters = MenuSection(section="Dinner Platters")

regular_pizza.save()
sicilian_pizza.save()
subs.save()
pasta.save()
salads.save()
platters.save()

# ------ Add Sizes to Database ------ #

one_size = Size(value="One Size")
small = Size(value="Small")
large = Size(value="Large")

small.save()
one_size.save()
large.save()

# ------ Add MenuItems to Database ------ #


# --- Regular Pizza category --- #

# - 0 Toppings - #
item = Item(name="Cheese Pizza - Plain")
item.save()
price_small = Price(item=item, size=small, base_price=12.20)
price_large = Price(item=item, size=large, base_price=17.45)
price_small.save()
price_large.save()

regular_pizza_0 = MenuItem(
    category=regular_pizza,
    name=item,
    number_of_possible_toppings=0
)
regular_pizza_0.save()

regular_pizza_0.available_sizes.add(small, large)
regular_pizza_0.prices.add(price_small, price_large)


# - 1 Topping - #
item = Item(name="Cheese Pizza - 1 Topping")
item.save()

price_small = Price(item=item, size=small, base_price=13.20)
price_large = Price(item=item, size=large, base_price=19.45)
price_small.save()
price_large.save()

regular_pizza_1 = MenuItem(
    category=regular_pizza,
    name=item,
    number_of_possible_toppings=1
)

regular_pizza_1.save()
regular_pizza_1.available_sizes.add(small, large)
regular_pizza_1.prices.add(price_small, price_large)
regular_pizza_1.available_topping_options.add(
    pepperoni, sausage, mushrooms, ham, canadian_bacon, pineapple, eggplant, tomato_basil, green_peppers, hamburger,
    spinach, artichoke, buffalo_chicken, barbecue_chicken, anchovies, black_olives, garlic, zucchini, onions
)


# - 2 Toppings - #
item = Item(name="Cheese Pizza - 2 Toppings")
item.save()

price_small = Price(item=item, size=small, base_price=14.70)
price_large = Price(item=item, size=large, base_price=21.45)
price_small.save()
price_large.save()

regular_pizza_2 = MenuItem(
    category=regular_pizza,
    name=item,
    number_of_possible_toppings=2
)

regular_pizza_2.save()
regular_pizza_2.available_sizes.add(small, large)
regular_pizza_2.prices.add(price_small, price_large)
regular_pizza_2.available_topping_options.add(
    pepperoni, sausage, mushrooms, ham, canadian_bacon, pineapple, eggplant, tomato_basil, green_peppers, hamburger,
    spinach, artichoke, buffalo_chicken, barbecue_chicken, anchovies, black_olives, garlic, zucchini, onions
)


# - 3 Toppings - #
item = Item(name="Cheese Pizza - 3 Toppings")
item.save()

price_small = Price(item=item, size=small, base_price=15.70)
price_large = Price(item=item, size=large, base_price=23.45)
price_small.save()
price_large.save()

regular_pizza_3 = MenuItem(
    category=regular_pizza,
    name=item,
    number_of_possible_toppings=3
)

regular_pizza_3.save()
regular_pizza_3.available_sizes.add(small, large)
regular_pizza_3.prices.add(price_small, price_large)
regular_pizza_3.available_topping_options.add(
    pepperoni, sausage, mushrooms, ham, canadian_bacon, pineapple, eggplant, tomato_basil, green_peppers, hamburger,
    spinach, artichoke, buffalo_chicken, barbecue_chicken, anchovies, black_olives, garlic, zucchini, onions
)

# - Special - #
item = Item(name="Special Cheese Pizza")
item.save()

price_small = Price(item=item, size=small, base_price=17.25)
price_large = Price(item=item, size=large, base_price=25.45)
price_small.save()
price_large.save()

regular_pizza_4 = MenuItem(
    category=regular_pizza,
    name=item,
    number_of_possible_toppings=0
)

regular_pizza_4.save()
regular_pizza_4.available_sizes.add(small, large)
regular_pizza_4.prices.add(price_small, price_large)


# --- Sicilian Pizza category --- #

# - 0 Toppings - #
item = Item(name="Sicilian Pizza - Plain")
item.save()

price_small = Price(item=item, size=small, base_price=23.45)
price_large = Price(item=item, size=large, base_price=37.70)
price_small.save()
price_large.save()

sicilian_pizza_0 = MenuItem(
    category=sicilian_pizza,
    name=item,
    number_of_possible_toppings=0
)
sicilian_pizza_0.save()

sicilian_pizza_0.available_sizes.add(small, large)
sicilian_pizza_0.prices.add(price_small, price_large)


# - 1 Topping - #
item = Item(name="Sicilian Pizza - 1 Topping")
item.save()

price_small = Price(item=item, size=small, base_price=25.45)
price_large = Price(item=item, size=large, base_price=39.70)
price_small.save()
price_large.save()

silician_pizza_1 = MenuItem(
    category=sicilian_pizza,
    name=item,
    number_of_possible_toppings=1
)

silician_pizza_1.save()
silician_pizza_1.available_sizes.add(small, large)
silician_pizza_1.prices.add(price_small, price_large)
silician_pizza_1.available_topping_options.add(
    pepperoni, sausage, mushrooms, ham, canadian_bacon, pineapple, eggplant, tomato_basil, green_peppers, hamburger,
    spinach, artichoke, buffalo_chicken, barbecue_chicken, anchovies, black_olives, garlic, zucchini, onions
)


# - 2 Toppings - #
item = Item(name="Sicilian Pizza - 2 Toppings")
item.save()

price_small = Price(item=item, size=small, base_price=27.45)
price_large = Price(item=item, size=large, base_price=41.70)
price_small.save()
price_large.save()

sicilian_pizza_2 = MenuItem(
    category=sicilian_pizza,
    name=item,
    number_of_possible_toppings=2
)

sicilian_pizza_2.save()
sicilian_pizza_2.available_sizes.add(small, large)
sicilian_pizza_2.prices.add(price_small, price_large)
sicilian_pizza_2.available_topping_options.add(
    pepperoni, sausage, mushrooms, ham, canadian_bacon, pineapple, eggplant, tomato_basil, green_peppers, hamburger,
    spinach, artichoke, buffalo_chicken, barbecue_chicken, anchovies, black_olives, garlic, zucchini, onions
)


# - 3 Toppings - #
item = Item(name="Sicilian Pizza - 3 Toppings")
item.save()

price_small = Price(item=item, size=small, base_price=28.45)
price_large = Price(item=item, size=large, base_price=43.70)
price_small.save()
price_large.save()

sicilian_pizza_3 = MenuItem(
    category=sicilian_pizza,
    name=item,
    number_of_possible_toppings=3
)

sicilian_pizza_3.save()
sicilian_pizza_3.available_sizes.add(small, large)
sicilian_pizza_3.prices.add(price_small, price_large)
sicilian_pizza_3.available_topping_options.add(
    pepperoni, sausage, mushrooms, ham, canadian_bacon, pineapple, eggplant, tomato_basil, green_peppers, hamburger,
    spinach, artichoke, buffalo_chicken, barbecue_chicken, anchovies, black_olives, garlic, zucchini, onions
)

# - Special - #
item = Item(name="Special Sicilian Pizza")
item.save()

price_small = Price(item=item, size=small, base_price=29.45)
price_large = Price(item=item, size=large, base_price=44.70)
price_small.save()
price_large.save()

sicilian_pizza_4 = MenuItem(
    category=sicilian_pizza,
    name=item,
    number_of_possible_toppings=0
)

sicilian_pizza_4.save()
sicilian_pizza_4.available_sizes.add(small, large)
sicilian_pizza_4.prices.add(price_small, price_large)


# --- Sub Category --- #

# - Cheese - #
item = Item(name="Cheese Sub")
item.save()

price_small = Price(item=item, size=small, base_price=6.50)
price_large = Price(item=item, size=large, base_price=7.95)
price_small.save()
price_large.save()

cheese_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

cheese_sub.save()
cheese_sub.available_sizes.add(small, large)
cheese_sub.prices.add(price_small, price_large)
cheese_sub.available_topping_options.add(extra_cheese)


# - Italian - #
item = Item(name="Italian Sub")
item.save()

price_small = Price(item=item, size=small, base_price=6.50)
price_large = Price(item=item, size=large, base_price=7.95)
price_small.save()
price_large.save()

italian_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

italian_sub.save()
italian_sub.available_sizes.add(small, large)
italian_sub.prices.add(price_small, price_large)
italian_sub.available_topping_options.add(extra_cheese)


# - Ham + Cheese - #
item = Item(name="Ham & Cheese Sub")
item.save()

price_small = Price(item=item, size=small, base_price=6.50)
price_large = Price(item=item, size=large, base_price=7.95)
price_small.save()
price_large.save()

ham_cheese_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

ham_cheese_sub.save()
ham_cheese_sub.available_sizes.add(small, large)
ham_cheese_sub.prices.add(price_small, price_large)
ham_cheese_sub.available_topping_options.add(extra_cheese)


# - Meatball Sub - #
item = Item(name="Meatball Sub")
item.save()

price_small = Price(item=item, size=small, base_price=6.50)
price_large = Price(item=item, size=large, base_price=7.95)
price_small.save()
price_large.save()

meatball_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

meatball_sub.save()
meatball_sub.available_sizes.add(small, large)
meatball_sub.prices.add(price_small, price_large)
meatball_sub.available_topping_options.add(extra_cheese)


# - Tuna Sub - #
item = Item(name="Tuna Sub")
item.save()

price_small = Price(item=item, size=small, base_price=6.50)
price_large = Price(item=item, size=large, base_price=7.95)
price_small.save()
price_large.save()

tuna_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

tuna_sub.save()
tuna_sub.available_sizes.add(small, large)
tuna_sub.prices.add(price_small, price_large)
tuna_sub.available_topping_options.add(extra_cheese)


# - Turkey Sub - #
item = Item(name="Turkey Sub")
item.save()

price_small = Price(item=item, size=small, base_price=6.50)
price_large = Price(item=item, size=large, base_price=8.50)
price_small.save()
price_large.save()

turkey_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

turkey_sub.save()
turkey_sub.available_sizes.add(small, large)
turkey_sub.prices.add(price_small, price_large)
turkey_sub.available_topping_options.add(extra_cheese)


# - Chicken Parmigiana Sub - #
item = Item(name="Chicken Parmigiana Sub")
item.save()

price_small = Price(item=item, size=small, base_price=7.50)
price_large = Price(item=item, size=large, base_price=8.50)
price_small.save()
price_large.save()

chick_parm_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

chick_parm_sub.save()
chick_parm_sub.available_sizes.add(small, large)
chick_parm_sub.prices.add(price_small, price_large)
chick_parm_sub.available_topping_options.add(extra_cheese)


# - Eggplant Parmigiana Sub - #
item = Item(name="Eggplant Parmigiana Sub")
item.save()

price_small = Price(item=item, size=small, base_price=6.50)
price_large = Price(item=item, size=large, base_price=7.95)
price_small.save()
price_large.save()

eggplant_parm_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

eggplant_parm_sub.save()
eggplant_parm_sub.available_sizes.add(small, large)
eggplant_parm_sub.prices.add(price_small, price_large)
eggplant_parm_sub.available_topping_options.add(extra_cheese)


# - Steak Sub - #
item = Item(name="Steak Sub")
item.save()

price_small = Price(item=item, size=small, base_price=6.50)
price_large = Price(item=item, size=large, base_price=7.95)
price_small.save()
price_large.save()

steak_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

steak_sub.save()
steak_sub.available_sizes.add(small, large)
steak_sub.prices.add(price_small, price_large)
steak_sub.available_topping_options.add(extra_cheese)


# - Steak + Cheese, Etc. Sub - #
item = Item(name="Steak + Cheese Sub")
item.save()

price_small = Price(item=item, size=small, base_price=6.95)
price_large = Price(item=item, size=large, base_price=8.50)
price_small.save()
price_large.save()

steak_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=4,
    price_per_additional_topping=0.50
)

steak_sub.save()
steak_sub.available_sizes.add(small, large)
steak_sub.prices.add(price_small, price_large)
steak_sub.available_topping_options.add(onions, green_peppers, mushrooms, extra_cheese)


# - Sausage Sub - #
item = Item(name="Sausage, Peppers & Onion Sub")
item.save()

price_large = Price(item=item, size=large, base_price=8.50)
price_small.save()
price_large.save()

sausage_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

sausage_sub.save()
sausage_sub.available_sizes.add(large)
sausage_sub.prices.add(price_large)
sausage_sub.available_topping_options.add(extra_cheese)


# - Hamburger Sub - #
item = Item(name="Hamburger Sub")
item.save()

price_small = Price(item=item, size=small, base_price=4.60)
price_large = Price(item=item, size=large, base_price=6.95)
price_small.save()
price_large.save()

hamburger_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

hamburger_sub.save()
hamburger_sub.available_sizes.add(small, large)
hamburger_sub.prices.add(price_small, price_large)
hamburger_sub.available_topping_options.add(extra_cheese)


# - Cheeseburger Sub - #
item = Item(name="Cheeseburger Sub")
item.save()

price_small = Price(item=item, size=small, base_price=5.10)
price_large = Price(item=item, size=large, base_price=7.45)
price_small.save()
price_large.save()

cheeseburger_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

cheeseburger_sub.save()
cheeseburger_sub.available_sizes.add(small, large)
cheeseburger_sub.prices.add(price_small, price_large)
cheeseburger_sub.available_topping_options.add(extra_cheese)


# - Fried Chicken Sub - #
item = Item(name="Fried Chicken Sub")
item.save()

price_small = Price(item=item, size=small, base_price=6.95)
price_large = Price(item=item, size=large, base_price=8.50)
price_small.save()
price_large.save()

fried_chick_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

fried_chick_sub.save()
fried_chick_sub.available_sizes.add(small, large)
fried_chick_sub.prices.add(price_small, price_large)
fried_chick_sub.available_topping_options.add(extra_cheese)


# - Veggie Sub - #
item = Item(name="Veggie Sub")
item.save()

price_small = Price(item=item, size=small, base_price=6.95)
price_large = Price(item=item, size=large, base_price=8.50)
price_small.save()
price_large.save()

veggie_sub = MenuItem(
    category=subs,
    name=item,
    number_of_possible_toppings=1,
    price_per_additional_topping=0.50
)

veggie_sub.save()
veggie_sub.available_sizes.add(small, large)
veggie_sub.prices.add(price_small, price_large)
veggie_sub.available_topping_options.add(extra_cheese)


# --- Pasta Category --- #

# - Ziti with Mozzarella - #
item = Item(name="Baked Ziti with Mozzarella")
item.save()

price_one_size = Price(item=item, size=one_size, base_price=6.50)
price_one_size.save()

ziti_mozz = MenuItem(
    category=pasta,
    name=item
)
ziti_mozz.save()
ziti_mozz.available_sizes.add(one_size)
ziti_mozz.prices.add(price_one_size)


# - Ziti with Meatballs - #
item = Item(name="Baked Ziti with Meatballs")
item.save()

price_one_size = Price(item=item, size=one_size, base_price=8.75)
price_one_size.save()

ziti_meatballs = MenuItem(
    category=pasta,
    name=item
)
ziti_meatballs.save()
ziti_meatballs.available_sizes.add(one_size)
ziti_meatballs.prices.add(price_one_size)

# - Ziti with Chicken - #
item = Item(name="Baked Ziti with Chicken")
item.save()

price_one_size = Price(item=item, size=one_size, base_price=9.75)
price_one_size.save()

ziti_chicken = MenuItem(
    category=pasta,
    name=item
)
ziti_chicken.save()
ziti_chicken.available_sizes.add(one_size)
ziti_chicken.prices.add(price_one_size)


# --- Salads category --- #

# - Garden Salad - #
item = Item(name="Garden Salad")
item.save()

price_one_size = Price(item=item, size=one_size, base_price=6.25)
price_one_size.save()

garden_salad = MenuItem(
    category=salads,
    name=item
)
garden_salad.save()
garden_salad.available_sizes.add(one_size)
garden_salad.prices.add(price_one_size)


# - Greek Salad - #
item = Item(name="Greek Salad")
item.save()

price_one_size = Price(item=item, size=one_size, base_price=8.25)
price_one_size.save()

greek_salad = MenuItem(
    category=salads,
    name=item
)
greek_salad.save()
greek_salad.available_sizes.add(one_size)
greek_salad.prices.add(price_one_size)


# - Antipasto Salad - #
item = Item(name="Antipasto")
item.save()

price_one_size = Price(item=item, size=one_size, base_price=8.25)
price_one_size.save()

antipasto = MenuItem(
    category=salads,
    name=item
)
antipasto.save()
antipasto.available_sizes.add(one_size)
antipasto.prices.add(price_one_size)


# - Tuna Salad - #
item = Item(name="Tuna Salad")
item.save()

price_one_size = Price(item=item, size=one_size, base_price=8.25)
price_one_size.save()

tuna_salad = MenuItem(
    category=salads,
    name=item
)
tuna_salad.save()
tuna_salad.available_sizes.add(one_size)
tuna_salad.prices.add(price_one_size)


# --- Dinner Platter category --- #

# - Garden Salad Platter - #
item = Item(name="Garden Salad Platter")
item.save()

price_small = Price(item=item, size=small, base_price=35.00)
price_large = Price(item=item, size=large, base_price=60.00)
price_small.save()
price_large.save()

garden_salad_platter = MenuItem(
    category=platters,
    name=item
)

garden_salad_platter.save()
garden_salad_platter.available_sizes.add(small, large)
garden_salad_platter.prices.add(price_small, price_large)

# - Greek Salad Platter - #
item = Item(name="Greek Salad Platter")
item.save()

price_small = Price(item=item, size=small, base_price=45.00)
price_large = Price(item=item, size=large, base_price=70.00)
price_small.save()
price_large.save()

greek_salad_platter = MenuItem(
    category=platters,
    name=item
)

greek_salad_platter.save()
greek_salad_platter.available_sizes.add(small, large)
greek_salad_platter.prices.add(price_small, price_large)


# - Antipasto Salad Platter - #
item = Item(name="Antipasto Platter")
item.save()

price_small = Price(item=item, size=small, base_price=45.00)
price_large = Price(item=item, size=large, base_price=70.00)
price_small.save()
price_large.save()

antipasto_platter = MenuItem(
    category=platters,
    name=item
)

antipasto_platter.save()
antipasto_platter.available_sizes.add(small, large)
antipasto_platter.prices.add(price_small, price_large)


# - Baked Ziti Platter - #
item = Item(name="Baked Ziti Platter")
item.save()

price_small = Price(item=item, size=small, base_price=35.00)
price_large = Price(item=item, size=large, base_price=60.00)
price_small.save()
price_large.save()

baked_ziti_platter = MenuItem(
    category=platters,
    name=item
)

baked_ziti_platter.save()
baked_ziti_platter.available_sizes.add(small, large)
baked_ziti_platter.prices.add(price_small, price_large)


# - Meatball Parm Platter - #
item = Item(name="Meatball Parmiagana Platter")
item.save()

price_small = Price(item=item, size=small, base_price=45.00)
price_large = Price(item=item, size=large, base_price=70.00)
price_small.save()
price_large.save()

meatball_parm_platter = MenuItem(
    category=platters,
    name=item
)

meatball_parm_platter.save()
meatball_parm_platter.available_sizes.add(small, large)
meatball_parm_platter.prices.add(price_small, price_large)

# - Chicken Parm Platter - #
item = Item(name="Chicken Parmiagana Platter")
item.save()

price_small = Price(item=item, size=small, base_price=45.00)
price_large = Price(item=item, size=large, base_price=80.00)
price_small.save()
price_large.save()

chicken_parm_platter = MenuItem(
    category=platters,
    name=item
)

chicken_parm_platter.save()
chicken_parm_platter.available_sizes.add(small, large)
chicken_parm_platter.prices.add(price_small, price_large)
