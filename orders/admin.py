from django.contrib import admin
from .models import Order, MenuSection, Item, Topping


class MenuItemAdmin(admin.ModelAdmin):
    exclude = ('toppings',)


admin.site.register(MenuSection)
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(Item, MenuItemAdmin)
