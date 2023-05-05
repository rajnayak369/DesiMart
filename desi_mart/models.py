from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Cart(models.Model):
    product = models.ForeignKey('desi_mart.Product', on_delete=models.CASCADE, related_name='carts')
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product},{self.quantity},{self.created_date}'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}, {self.address}'

    class Meta:
        db_table = 'customer'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.customer.save()

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class LineItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey('desi_mart.Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('desi_mart.Cart', on_delete=models.CASCADE)
    order = models.ForeignKey('desi_mart.Order', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity},{self.product},{self.cart},{self.order},{self.created_date}'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    imageLink = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

class Order(models.Model):
    customer = models.ForeignKey('desi_mart.Customer', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer},{self.created_date}'