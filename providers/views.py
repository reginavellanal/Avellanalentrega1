from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from providers.models import Provider
from providers.forms import Providerform

def providers_list(request):
    providers = Provider.objects.filter(is_active = True)
    context = {
        'providers':providers
    }
    return render(request, 'list_providers.html', context=context)

class ProvidersListView(LoginRequiredMixin, ListView):
    model = Provider
    template_name = 'list_providers.html'
    queryset = Provider.objects.filter(is_active = True)

def providers_create(request):
    if request.method == 'GET':
        context = {
            'form': Providerform()
        }
        return render(request, 'create_provider.html', context=context)
    
    elif request.method == 'POST':
        form = Providerform(request.POST)
        if form.is_valid():
            Provider.objects.create(
                name = form.cleaned_data['name'],
                adress = form.cleaned_data['adress'],
                phone_number = form.cleaned_data['phone_number'],
                email = form.cleaned_data['email'],

            )
            context = {
                'message': 'Proveedor añadido correctamente'
            }
            return render(request, 'create_provider.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': Providerform()
            }
            return render(request, 'create_provider.html', context=context)

class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'create_provider.html'
    fields = '__all__'
    success_url = '/providers/list_providers/'

def providers_update(request, pk):

    provider = Provider.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': Providerform(
                initial={
                    'name':provider.name,
                    'adress':provider.adress,
                    'phone_number':provider.phone_number,
                    'email':provider.email,
                }
            )
        }
        return render(request, 'update_provider.html', context=context)
    
    elif request.method == 'POST':
        form = Providerform(request.POST)
        if form.is_valid():
            provider.name = form.cleaned_data['name']
            provider.adress = form.cleaned_data['adress']
            provider.phone_number = form.cleaned_data['phone_number']
            provider.email = form.cleaned_data['email']
            provider.save()

            context = {
                'message': 'Proveedor actualizado correctamente'
            }
            return render(request, 'update_provider.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': Providerform()
            }
            return render(request, 'update_provider.html', context=context)

class ProviderUpdateView(UpdateView):
    model = Provider
    template_name = 'update_provider.html'
    fields = '__all__'
    success_url = '/providers/list_providers/'


class ProviderDeleteView(DeleteView):
    model = Provider
    template_name = 'delete_provider.html'
    success_url = '/providers/list_providers/'
