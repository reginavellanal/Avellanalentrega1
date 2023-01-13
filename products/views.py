from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products, Categorie, Panaderia
from products.forms import ProductsForm, CategorieForm, PanaderiaForm

#crearemos los productos del modelo Products

def create_product(request):
    if request.method == 'GET':
        context = {
            'form': ProductsForm()
        }
        return render(request, 'create_product.html', context=context)
    
    elif request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock']
            )
            context = {
                'message': 'Departamento añadido correctamente'
            }
            return render(request, 'create_product.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductsForm()
            }
            return render(request, 'create_product.html', context=context)

#para poder ver los productos creados creo la lista de productos

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Products.objects.filter(name__contains=search)
    else:
        products = Products.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'list_products.html', context=context)

#creo las categorias#

def create_categorie(request):
    if request.method == 'GET':
        context = {
            'form': CategorieForm()
        }
        return render(request, 'create_categorie.html', context=context)
    
    elif request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            Categorie.objects.create(
                name=form.cleaned_data['name']
            )
            context = {
                'message': 'Region añadida correctamente'
            }
            return render(request, 'create_categorie.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': CategorieForm()
            }
            return render(request, 'create_categorie.html', context=context)


def list_categories(request):
    all_categories = Categorie.objects.all()
    context = {
        'categories':all_categories
    }
    return render(request, 'list_categories.html', context=context)

def create_panaderia(request):
    if request.method == 'GET':
        context = {
            'form': PanaderiaForm()
        }
        return render(request, 'create_panaderia.html', context=context)
    
    elif request.method == 'POST':
        form = PanaderiaForm(request.POST)
        if form.is_valid():
            Panaderia.objects.create(
                name=form.cleaned_data['name'],
                horario=form.cleaned_data['horario'],
                stock=form.cleaned_data['stock']
            )
            context = {
                'message': 'Panaderia añadida correctamente'
            }
            return render(request, 'create_panaderia.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': PanaderiaForm()
            }
            return render(request, 'create_panaderia.html', context=context)


def list_panaderias(request):
    all_panaderias = Panaderia.objects.all()
    context = {
        'panaderias':all_panaderias
    }
    return render(request, 'list_panaderias.html', context=context)

