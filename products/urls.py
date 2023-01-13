from django.urls import path
from products.views import create_product, list_products, list_categories, create_categorie, create_panaderia, list_panaderias

urlpatterns = [
    path('create-product/', create_product),
    path('list-products/', list_products),

    path('create-categorie/', create_categorie),
    path('list-categories/', list_categories),

    path('create-panaderia/', create_panaderia),
    path('list-panaderias/', list_panaderias), 

]