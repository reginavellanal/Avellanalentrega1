from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={})

def saludo_inicial(request):
    return HttpResponse("Bienvenidos a la ruta del bizcocho uruguayo")

def vista_con_template(request):
    return render(request, 'template.html', context={})

def saludo_template(request):
    nombre = 'Regina'
    context = {
        'nombre': nombre,
    }
    return render(request, 'saludo.html', context=context)