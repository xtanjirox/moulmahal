from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from core import models
from core import tables
from core import filters

from .base import BaseListView, FormViewMixin, BaseDeleteView


class OrderItemsListView(BaseListView):
    model = models.OrderItems
    table_class = tables.OrderItemsTable
    filter_class = filters.OrderItemsFilter
    table_pagination = False
    create_url = reverse_lazy('order_items-create')
    segment = 'order_items'


class OrderItemCreateView(CreateView, FormViewMixin):
    model = models.OrderItems
    template_name = 'generic/create.html'
    fields = '__all__'
    segment = 'order_items'
    success_url = reverse_lazy('order_items-list')


class OrderItemUpdateView(UpdateView, FormViewMixin):
    model = models.OrderItems
    template_name = 'generic/detail.html'
    fields = '__all__'
    segment = 'order_items'


class OrderItemDeleteView(BaseDeleteView):
    model = models.OrderItems
    success_url = reverse_lazy('order_items-list')
