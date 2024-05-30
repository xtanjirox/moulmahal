from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from core import models
from core import tables
from core import filters

from .base import BaseListView, FormViewMixin, BaseDeleteView


class ProductListView(BaseListView):
    model = models.Products
    table_class = tables.ProductsTable
    filter_class = filters.ProductFilter
    table_pagination = False
    create_url = reverse_lazy('products-create')
    segment = 'products'
    get_stats = True


class ProductCreateView(CreateView, FormViewMixin):
    model = models.Products
    template_name = 'generic/create.html'
    fields = '__all__'
    segment = 'products'
    success_url = reverse_lazy('products-list')


class ProductUpdateView(UpdateView, FormViewMixin):
    model = models.Products
    template_name = 'generic/detail.html'
    fields = '__all__'
    segment = 'products'


class ProductDeleteView(BaseDeleteView):
    model = models.Products
    success_url = reverse_lazy('products-list')
