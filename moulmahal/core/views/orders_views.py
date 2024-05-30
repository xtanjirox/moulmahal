from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from core import models
from core import tables
from core import filters

from .base import BaseListView, FormViewMixin, BaseDeleteView


class OrderListView(BaseListView):
    model = models.Orders
    table_class = tables.OrdersTable
    filter_class = filters.OrderFilter
    table_pagination = False
    create_url = reverse_lazy('orders-create')
    segment = 'orders'


class OrderCreateView(CreateView, FormViewMixin):
    model = models.Orders
    template_name = 'generic/create.html'
    fields = '__all__'
    segment = 'orders'
    success_url = reverse_lazy('orders-list')


class OrderUpdateView(UpdateView, FormViewMixin):
    model = models.Orders
    template_name = 'generic/detail.html'
    fields = '__all__'
    segment = 'orders'


class OrderDeleteView(BaseDeleteView):
    model = models.Orders
    success_url = reverse_lazy('orders-list')
