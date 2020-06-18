from .models import *


class MenuDB:

    def __init__(self):
        self.categories = MenuSection.objects.all()

    def get_items_by_category(self, category):
        return MenuItem.objects.filter(category__name=category)
