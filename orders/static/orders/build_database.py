"""
Sets up database from scratch, if necessary, to reflect Pinnochio’s Pizza on 07/2019
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

small = Size(value="Small")
regular = Size(value="Regular")
large = Size(value="Large")

small.save()
regular.save()
large.save()

# ------ Add Items to Database ------ #


# - Regular Pizza category - #

s_regular_pizza_0 = Item(
    category=regular_pizza,
    name="Cheese",
    size=small,
    number_of_toppings=0,
    price=12.20
)

l_regular_pizza_0 = Item(
    category=regular_pizza,
    name="Cheese Pizza",
    size=large,
    number_of_toppings=0,
    price=17.45
)

s_regular_pizza_1 = Item(
    category=regular_pizza,
    name="Cheese Pizza - 1 Topping",
    size=small,
    number_of_toppings=1,
    price=13.20
)

l_regular_pizza_1 = Item(
    category=regular_pizza,
    name="Cheese Pizza - 1 Topping",
    size=large,
    number_of_toppings=1,
    price=19.45
)

s_regular_pizza_2 = Item(
    category=regular_pizza,
    name="Cheese Pizza - 2 Toppings",
    size=small,
    number_of_toppings=2,
    price=14.70
)

l_regular_pizza_2 = Item(
    category=regular_pizza,
    name="Cheese Pizza - 2 Toppings",
    size=large,
    number_of_toppings=2,
    price=21.45
)

s_regular_pizza_3 = Item(
    category=regular_pizza,
    name="Cheese Pizza - 3 Toppings",
    size=small,
    number_of_toppings=3,
    price=15.70
)

l_regular_pizza_3 = Item(
    category=regular_pizza,
    name="Cheese Pizza - 3 Toppings",
    size=large,
    number_of_toppings=3,
    price=23.45
)


s_regular_pizza_special = Item(
    category=regular_pizza,
    name="Special",
    size=small,
    number_of_toppings=0,
    price=17.25
)

l_regular_pizza_special = Item(
    category=regular_pizza,
    name="Special",
    size=large,
    number_of_toppings=0,
    price=25.45
)

s_regular_pizza_0.save()
l_regular_pizza_0.save()

s_regular_pizza_1.save()
l_regular_pizza_1.save()

s_regular_pizza_2.save()
l_regular_pizza_2.save()

s_regular_pizza_3.save()
l_regular_pizza_3.save()

s_regular_pizza_special.save()
l_regular_pizza_special.save()


# - Sicilian Pizza category - #

s_sicilian_pizza_0 = Item(
    category=sicilian_pizza,
    name="Cheese Pizza",
    size=small,
    number_of_toppings=0,
    price=23.45
)

l_sicilian_pizza_0 = Item(
    category=sicilian_pizza,
    name="Cheese Pizza",
    size=large,
    number_of_toppings=0,
    price=37.70
)

s_sicilian_pizza_1 = Item(
    category=sicilian_pizza,
    name="Cheese Pizza - 1 Topping",
    size=small,
    number_of_toppings=1,
    price=25.45
)

l_sicilian_pizza_1 = Item(
    category=sicilian_pizza,
    name="Cheese Pizza - 1 Topping",
    size=large,
    number_of_toppings=1,
    price=39.70
)

s_sicilian_pizza_2 = Item(
    category=sicilian_pizza,
    name="Cheese Pizza - 2 Toppings",
    size=small,
    number_of_toppings=2,
    price=27.45
)

l_sicilian_pizza_2 = Item(
    category=sicilian_pizza,
    name="Cheese Pizza - 2 Toppings",
    size=large,
    number_of_toppings=2,
    price=41.70
)

s_sicilian_pizza_3 = Item(
    category=sicilian_pizza,
    name="Cheese Pizza - 3 Toppings",
    size=small,
    number_of_toppings=3,
    price=28.45
)

l_sicilian_pizza_3 = Item(
    category=sicilian_pizza,
    name="Cheese Pizza - 3 Toppings",
    size=large,
    number_of_toppings=3,
    price=43.70
)

s_sicilian_pizza_special = Item(
    category=sicilian_pizza,
    name="Special",
    size=small,
    number_of_toppings=3,
    price=29.45
)

l_sicilian_pizza_special = Item(
    category=sicilian_pizza,
    name="Special",
    size=large,
    number_of_toppings=3,
    price=44.70
)

s_sicilian_pizza_0.save()
l_sicilian_pizza_0.save()

s_sicilian_pizza_1.save()
l_sicilian_pizza_1.save()

s_sicilian_pizza_2.save()
l_sicilian_pizza_2.save()

s_sicilian_pizza_3.save()
l_sicilian_pizza_3.save()

s_sicilian_pizza_special.save()
l_sicilian_pizza_special.save()


# - Sub category - #

s_cheese_sub = Item(
    category=subs,
    name="Cheese",
    size=small,
    number_of_toppings=0,
    price=6.50
)

l_cheese_sub = Item(
    category=subs,
    name="Cheese Sub",
    size=large,
    number_of_toppings=0,
    price=7.95
)

s_italian_sub = Item(
    category=subs,
    name="Italian Sub",
    size=small,
    number_of_toppings=0,
    price=6.50
)

l_italian_sub = Item(
    category=subs,
    name="Italian Sub",
    size=large,
    number_of_toppings=0,
    price=7.95
)

s_ham_sub = Item(
    category=subs,
    name="Ham & Cheese Sub",
    size=small,
    number_of_toppings=0,
    price=6.50
)

l_ham_sub = Item(
    category=subs,
    name="Ham & Cheese Sub",
    size=large,
    number_of_toppings=0,
    price=7.95
)

s_meatball_sub = Item(
    category=subs,
    name="Meatball Sub",
    size=small,
    number_of_toppings=0,
    price=6.50
)

l_meatball_sub = Item(
    category=subs,
    name="Meatball Sub",
    size=large,
    number_of_toppings=0,
    price=7.95
)

s_tuna_sub = Item(
    category=subs,
    name="Tuna Sub",
    size=small,
    number_of_toppings=0,
    price=6.50
)

l_tuna_sub = Item(
    category=subs,
    name="Tuna Sub",
    size=large,
    number_of_toppings=0,
    price=7.95
)

s_turkey_sub = Item(
    category=subs,
    name="Turkey Sub",
    size=small,
    number_of_toppings=0,
    price=7.50
)

l_turkey_sub = Item(
    category=subs,
    name="Turkey Sub",
    size=large,
    number_of_toppings=0,
    price=8.50
)

s_chicken_parm_sub = Item(
    category=subs,
    name="Chicken Parmigiana Sub",
    size=small,
    number_of_toppings=0,
    price=7.50
)

l_chicken_parm_sub = Item(
    category=subs,
    name="Chicken Parmigiana Sub",
    size=large,
    number_of_toppings=0,
    price=8.50
)

s_eggplant_parm_sub = Item(
    category=subs,
    name="Eggplant Parmigiana Sub",
    size=small,
    number_of_toppings=0,
    price=6.50
)

l_eggplant_parm_sub = Item(
    category=subs,
    name="Eggplant Parmigiana Sub",
    size=large,
    number_of_toppings=0,
    price=7.95
)

s_steak_sub = Item(
    category=subs,
    name="Steak Sub",
    size=small,
    number_of_toppings=0,
    price=6.50
)

l_steak_sub = Item(
    category=subs,
    name="Steak Sub",
    size=large,
    number_of_toppings=0,
    price=7.95
)

s_steak_cheese_sub_0 = Item(
    category=subs,
    name="Steak & Cheese Sub",
    size=small,
    number_of_toppings=0,
    price=6.95
)

l_steak_cheese_sub_0 = Item(
    category=subs,
    name="Steak & Cheese Sub",
    size=large,
    number_of_toppings=0,
    price=8.50
)

s_steak_cheese_sub_1 = Item(
    category=subs,
    name="Steak & Cheese Sub",
    size=small,
    number_of_toppings=1,
    price=7.45
)

l_steak_cheese_sub_1 = Item(
    category=subs,
    name="Steak & Cheese Sub",
    size=large,
    number_of_toppings=1,
    price=9.00
)

s_steak_cheese_sub_2 = Item(
    category=subs,
    name="Steak & Cheese Sub",
    size=small,
    number_of_toppings=2,
    price=7.95
)

l_steak_cheese_sub_2 = Item(
    category=subs,
    name="Steak & Cheese Sub",
    size=large,
    number_of_toppings=2,
    price=9.50
)
s_steak_cheese_sub_3 = Item(
    category=subs,
    name="Steak & Cheese Sub",
    size=small,
    number_of_toppings=3,
    price=8.45
)

l_steak_cheese_sub_3 = Item(
    category=subs,
    name="Steak & Cheese Sub",
    size=large,
    number_of_toppings=3,
    price=10.00
)

sausage_sub = Item(
    category=subs,
    name="Sausage, Pepper & Onion Sub",
    size=large,
    number_of_toppings=0,
    price=8.50
)

s_hamburger = Item(
    category=subs,
    name="Hamburger",
    size=small,
    number_of_toppings=0,
    price=4.60
)

l_hamburger = Item(
    category=subs,
    name="Hamburger",
    size=large,
    number_of_toppings=0,
    price=6.95
)

s_cheeseburger = Item(
    category=subs,
    name="Cheeseburger",
    size=small,
    number_of_toppings=0,
    price=5.10
)

l_cheeseburger = Item(
    category=subs,
    name="Cheeseburger",
    size=large,
    number_of_toppings=0,
    price=7.45
)

s_fried_chicken = Item(
    category=subs,
    name="Fried Chicken Sub",
    size=small,
    number_of_toppings=0,
    price=6.95
)

l_fried_chicken = Item(
    category=subs,
    name="Fried Chicken Sub",
    size=large,
    number_of_toppings=0,
    price=8.50
)

s_veggie = Item(
    category=subs,
    name="Veggie Sub",
    size=small,
    number_of_toppings=0,
    price=6.95
)

l_veggie = Item(
    category=subs,
    name="Veggie Sub",
    size=large,
    number_of_toppings=0,
    price=8.50
)

s_cheese_sub.save()
l_cheese_sub.save()

s_italian_sub.save()
l_italian_sub.save()

s_ham_sub.save()
l_ham_sub.save()

s_meatball_sub.save()
l_meatball_sub.save()

s_tuna_sub.save()
l_tuna_sub.save()

s_turkey_sub.save()
l_turkey_sub.save()

s_chicken_parm_sub.save()
l_chicken_parm_sub.save()

s_eggplant_parm_sub.save()
l_eggplant_parm_sub.save()

s_steak_sub.save()
l_steak_sub.save()

s_steak_cheese_sub_0.save()
l_steak_cheese_sub_0.save()

s_steak_cheese_sub_1.save()
l_steak_cheese_sub_1.save()

s_steak_cheese_sub_2.save()
l_steak_cheese_sub_2.save()

s_steak_cheese_sub_3.save()
l_steak_cheese_sub_3.save()

sausage_sub.save()

s_hamburger.save()
l_hamburger.save()

s_cheeseburger.save()
l_cheeseburger.save()

s_fried_chicken.save()
l_fried_chicken.save()

s_veggie.save()
l_veggie.save()


# - Pasta category - #


ziti_mozz = Item(
    category=pasta,
    name="Baked Ziti with Mozzarella",
    size=regular,
    price=6.50
)

ziti_meatballs = Item(
    category=pasta,
    name="Baked Ziti with Meatballs",
    size=regular,
    price=8.75
)

ziti_chicken = Item(
    category=pasta,
    name="Baked Ziti with Chicken",
    size=regular,
    price=9.75
)

ziti_mozz.save()
ziti_meatballs.save()
ziti_chicken.save()


# - Salads category - #

garden_salad = Item(
    category=salads,
    name="Garden Salad",
    size=regular,
    price=6.25
)

greek_salad = Item(
    category=salads,
    name="Greek Salad",
    size=regular,
    price=8.25
)

antipasto = Item(
    category=salads,
    name="Antipasto Salad",
    size=regular,
    price=8.25
)

tuna_salad = Item(
    category=salads,
    name="Salad w/ Tuna",
    size=regular,
    price=8.25
)

garden_salad.save()
greek_salad.save()
antipasto.save()
tuna_salad.save()


# - Dinner Platter category - #

s_garden_salad_platter = Item(
    category=platters,
    name="Garden Salad Platter",
    size=small,
    price=35.00
)

l_garden_salad_platter = Item(
    category=platters,
    name="Garden Salad Platter",
    size=large,
    price=60.00
)

s_greek_salad_platter = Item(
    category=platters,
    name="Greek Salad Platter",
    size=small,
    price=45.00
)

l_greek_salad_platter = Item(
    category=platters,
    name="Greek Salad Platter",
    size=large,
    price=70.00
)

s_antipasto_salad_platter = Item(
    category=platters,
    name="Antipasto Salad Platter",
    size=small,
    price=45.00
)

l_antipasto_salad_platter = Item(
    category=platters,
    name="Antipasto Salad Platter",
    size=large,
    price=70.00
)

s_baked_ziti_platter = Item(
    category=platters,
    name="Baked Ziti Platter",
    size=small,
    price=35.00
)

l_baked_ziti_platter = Item(
    category=platters,
    name="Baked Ziti Platter",
    size=large,
    price=60.00
)

s_meat_parm_platter = Item(
    category=platters,
    name="Meatball Parmigiana Platter",
    size=small,
    price=45.00
)

l_meat_parm_platter = Item(
    category=platters,
    name="Meatball Parmigiana Platter",
    size=large,
    price=70.00
)

s_chicken_parm_platter = Item(
    category=platters,
    name="Chicken Parmigiana Platter",
    size=small,
    price=45.00
)

l_chicken_parm_platter = Item(
    category=platters,
    name="Chicken Parmigiana Platter",
    size=large,
    price=80.00
)

s_garden_salad_platter.save()
l_garden_salad_platter.save()

s_greek_salad_platter.save()
l_greek_salad_platter.save()

s_antipasto_salad_platter.save()
l_antipasto_salad_platter.save()

s_baked_ziti_platter.save()
l_baked_ziti_platter.save()

s_meat_parm_platter.save()
l_meat_parm_platter.save()

s_chicken_parm_platter.save()
l_chicken_parm_platter.save()
