from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from products.models import Products, Panaderia

##PRODUCTS SON LOS DEPARTAMENTOS DE URUGUAY QUE SE RECCOREN PARA LAS PANADERIAS
class ProductsListView(ListView):
    model = Products
    template_name = 'list_products.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(name__contains=search)
        return queryset

class ProductsCreateView(CreateView):
    model = Products
    template_name = 'create_product.html'
    fields = '__all__'
    success_url = '/products/list-products/'
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        product = Products.objects.filter(name=name)
        if product.exists():
            form.add_error('name', 'Ya existe un departamento con este nombre.')
            return self.form_invalid(form)
        return super().form_valid(form)

class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    template_name = 'update_product.html'
    fields = '__all__'
    success_url = '/products/list-products/'

class ProductsDeleteView(LoginRequiredMixin, DeleteView):
    model = Products
    template_name = 'delete_product.html'
    success_url = '/products/list-products/'

##PANADERIAS

class PanaderiaListView(ListView):
    model = Panaderia
    template_name = 'list_panaderias.html'

class PanaderiaCreateView(CreateView):
    model = Panaderia
    template_name = 'create_panaderia.html'
    fields = '__all__'
    success_url = '/products/list-panaderias/'

class PanaderiaUpdateView(LoginRequiredMixin, UpdateView):
    model = Panaderia
    template_name = 'update_panaderia.html'
    fields = '__all__'
    success_url = '/products/list-panaderias/'

class PanaderiaDeleteView(LoginRequiredMixin, DeleteView):
    model = Panaderia
    template_name = 'delete_panaderia.html'
    success_url = '/products/list-panaderias/'


##ESPACIO SOBRE MI
def about_me(request):
    return render(request, 'about_me.html')
