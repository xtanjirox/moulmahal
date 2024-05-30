from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from core import models
from core import tables
from core import filters

from .base import BaseListView, FormViewMixin, BaseDeleteView


class ClientListView(BaseListView):
    model = models.Clients
    table_class = tables.ClientsTable
    filter_class = filters.ClientFilter
    table_pagination = False
    create_url = reverse_lazy('clients-create')
    segment = 'clients'


class ClientCreateView(CreateView, FormViewMixin):
    model = models.Clients
    template_name = 'generic/create.html'
    fields = '__all__'
    segment = 'clients'
    success_url = reverse_lazy('clients-list')


class ClientUpdateView(UpdateView, FormViewMixin):
    model = models.Clients
    template_name = 'generic/detail.html'
    fields = '__all__'
    segment = 'clients'


class ClientDeleteView(BaseDeleteView):
    model = models.Clients
    success_url = reverse_lazy('clients-list')
