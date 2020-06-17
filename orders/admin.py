from django.contrib import admin
from .models import Order, MenuSection, MenuItem, CustomerItem, Topping, Price, Item


class ItemInline(admin.StackedInline):
    model = Item

class MenuPriceInline(admin.StackedInline):
    model = MenuItem.prices.through
    inlines = [ItemInline, ]
    extra = 1

class PriceAdmin(admin.ModelAdmin):
    inlines = [MenuPriceInline,]


class MenuItemAdmin(admin.ModelAdmin):
    filter_horizontal = ("prices",)


admin.site.register(MenuSection)
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(CustomerItem)
admin.site.register(Price, PriceAdmin)
admin.site.register(Item)
