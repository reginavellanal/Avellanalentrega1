from django.contrib import admin

# Register your models here.
from products.models import Products

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
#admin.site.register(Products)

from products.models import Categorie
admin.site.register(Categorie)

from products.models import Panaderia
admin.site.register(Panaderia)