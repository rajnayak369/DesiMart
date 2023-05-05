from django.contrib import admin

# Register your models here.
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'imageLink', 'price', 'discount_price',
                    'in_stock']
    list_filter = ['in_stock']
    list_editable = ['discount_price', 'in_stock']
