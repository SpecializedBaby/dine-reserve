from django.contrib import admin
from .models import DishType, Dish, Menu, Customer, Cart, Reservation


admin.site.register(DishType)
admin.site.register(Dish)
admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Reservation)
