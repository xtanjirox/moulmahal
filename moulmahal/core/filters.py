import django_filters
from django import forms
from . import models
from django_select2 import forms as s2forms


class ProductFilter(django_filters.FilterSet):
    product_title = django_filters.CharFilter('product_title', lookup_expr='icontains')

    class Meta:
        model = models.Products
        fields = ['product_title', ]


class CostFilter(django_filters.FilterSet):
    cost_type = django_filters.CharFilter('cost_type', lookup_expr='icontains')
    spending_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = models.Costs
        fields = ['cost_type', 'spending_date']


class ClientFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter('client_name', lookup_expr='icontains')
    client_phone = django_filters.CharFilter('client_phone', lookup_expr='icontains')

    class Meta:
        model = models.Clients
        fields = ['client_name', 'client_phone']


class OrderFilter(django_filters.FilterSet):
    client = django_filters.CharFilter('client__client_name', lookup_expr='icontains')

    class Meta:
        model = models.Orders
        fields = ['client']


class OrderItemsFilter(django_filters.FilterSet):
    order = django_filters.CharFilter('order__order_id', lookup_expr='icontains')
    product = django_filters.CharFilter('product__product_title', lookup_expr='icontains')

    class Meta:
        model = models.OrderItems
        fields = ['order', 'product']
