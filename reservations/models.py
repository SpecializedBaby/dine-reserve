from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    dishes = models.ManyToManyField(Dish, related_name="menus")

    def __str__(self):
        return self.name


class Customer(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.username


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dishes = models.ManyToManyField(Dish, related_name="carts")

    def __str__(self):
        return f"Cart {self.id} for {self.customer.username}"


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField(blank=True, null=True)
    number_of_people = models.IntegerField()
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.SET_NULL)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation {self.id} by {self.customer.username} on {self.reservation_date}"
