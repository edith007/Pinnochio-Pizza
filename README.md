# Pinnochio-Pizza

## I. About

This project, _Pinnochio's Pizza & Subs_, is an interactive Django web application that surfaces the menu of an existing restaurant in Cambridge, Massachusetts and allows customer's to customize their order, add items to their cart and ultimately place food orders.Administrators also have access to page that allows them to view all orders and their current statuses.

![](https://imgur.com/CQaurbX)

If their credentials do not exist, a customer may register for an account by providing a username, name and email. If the username is already taken, the customer will be prompted to provide another username. If the username is available, their account will be created and the user will be redirected back to the login page to login.

Once the customer has been authenticated, they will be brought to the website's main landing page, which surfaces all the items on the Pinnochio's Pizza & Subs menu (shown below).

![](https://imgur.com/zNwA3pr)

![](https://imgur.com/cVgjeP1)


#### Administrators Only

![](https://imgur.com/7Q0kxpP)

## II. Website Components

### Django

This application uses Django, a high-level python framework for web development. Django facilitates
in (1) the creation of a database and migrations of the database model, (2) configuration of routes (3) templating of html
 pages (as above) and (4) sending emails to  website users, among other features. This Django project utilizes only one app, `orders`.

#### a. Database Model

The database model underlying this project can be found in `orders/database.py`. This model
includes the following model classes:
* `MenuSection()`: representing a single menu section (i.e., Subs)
* `Size()`: represents available sizes of items (i.e., small)
* `Topping()`: represents available toppings (i.e., onions)
* `Item()`: represents the an individual menu item name only, for model purposes
* `Price()`: represents a unique combination of price with size and item
* `MenuItem()`: represents a single item on the menu in its entirety, designed with available
customer options in mind
* `CustomerItem()`: a customized item created be a customer (i.e., small cheese pizza with onions costing $14.40)
* `Order()`: an order object representing all CustomerItems() in that order, capturing time of actions of that order.

The database was modeled off of the menu on the real _Pinnochio's Pizza & Subs_ website
found here: http://www.pinocchiospizza.net/menu.html.

This project utilizes a sqlite relational database (the Django default) that was created using the code stored in
`orders/build_database.py`. This file can be used to create each item in the database, with its correct relationships,
in the case that the database needs to be regenerated again. Because the database, in it's current state, is quite small, it
was committed as part of this project (see `db.sqlite3`).

If changes to the database model are necessary, see the section entitled `Develop`  under`IV. Usage Locally`  
for more information on database migrations. Additions, changes, and deletions to individual items in the database
can be accomplished by logging into the admin UI with a `superuser` login at the `/admin` endpoint of the webpage.

#### b. Routes

Routes for the website are configured in this applications `orders/views.py` file, allowing
for users to login, logout, register, add items to cart, submit an order and view all orders (for administrators).
Urls for these routes can be found in the associated `orders/urls.py` file.

#### c. Settings

Settings for the project were updated from their default settings in the `pizza/settings.py` file.
In addition to adding the `orders` app to  `INSTALLED_APPS`, at the bottom of the page, changes were made to settings
relevant for enabling the `orders` application to send emails. An email address was created on Google.com for this
application to use in sending emails (`pinnochiopizzaandsubs@gmail.com`), with a password accessible via environmental
variables (see `Setup` below).

### HTML + CSS

This application includes several HTML pages, each extending a single template, `orders/template.html`:
* `login.html`: surfaces the login page for the user
* `register.html`: surfaces ther registration page for the user
* `index.html`: surfaces the main menu page of the website
* `cart.html`: shows the customer cart
* `all_order.html`: shows all orders ever placed for site administrators only.

Templating was accomplished using the Django html template language (see more on Django above).

All formatting for the website is controlled by a single stylesheet, found in
`orders/static/orders/styles.css`. Images and icons used in this website can similarly be found under `orders/static/img/`.


## III. Usage Locally

### Run

With the above steps completed, you may deploy the website locally and review it:
```
(venv) $ python manage.py runserver
```
Use the resulting url printed out by Django in any browser to see the website in action.

### Develop

Use the following tips in making changes to this application.

#### a. Database migrations

To run database migrations, after making changes to the database model in `orders/models.py`, use the following commands:
```
(venv) $ python manage.py makemigrations
(venv) $ python migrate --run-syncdb
```
Confirm that migrations were successful by identifying a new file in the `orders/migrations` directory.

#### b. Create new administrator (`superuser`)

Administrators have access to the Django database UI for editing database items and the ability to view all orders
from the website. Create a new administrator using the following command:

```
(venv) $ python manage.py createsuperuser
```

#### b. Tests

Django facilities testing by extending python's unittest testing framework. Tests for this application can
be run via:
```
(venv) $ python manage.py test
```
