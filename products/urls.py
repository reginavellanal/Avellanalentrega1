from django.urls import path
from products.views import PanaderiaListView, PanaderiaCreateView, PanaderiaUpdateView, PanaderiaDeleteView, ProductsListView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView, about_me

urlpatterns = [
    path('list-panaderias/', PanaderiaListView.as_view(), name='panaderias_list'),
    path('create-panaderia/', PanaderiaCreateView.as_view(), name='create_panaderia'),
    path('update_panaderia/<int:pk>/', PanaderiaUpdateView.as_view(), name='panaderia_update'),
    path('delete_panaderia/<int:pk>/', PanaderiaDeleteView.as_view(), name='panaderia_delete'),

    path('list-products/', ProductsListView.as_view(), name='products_list'),
    path('create-product/', ProductsCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductsUpdateView.as_view(), name='product_update'),
    path('delete_product/<int:pk>/', ProductsDeleteView.as_view(), name='product_delete'),

    path('about/', about_me, name='about_me'),

]