from django.urls import path
from providers.views import providers_list, providers_create, providers_update, ProvidersListView, ProviderCreateView, ProviderDeleteView, ProviderUpdateView

urlpatterns = [
    path('list_providers/', ProvidersListView.as_view(), name='providers_list'),
    path('create_provider/', ProviderCreateView.as_view(), name='providers_create'),
    path('update_provider/<int:pk>/', ProviderUpdateView.as_view(), name='providers_update'),
    path('delete_provider/<int:pk>/', ProviderDeleteView.as_view(), name='providers_delete'),

]