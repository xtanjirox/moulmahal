from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from core import models
from core import tables
from core import filters

from .base import BaseListView, FormViewMixin, BaseDeleteView


class CostListView(BaseListView):
    model = models.Costs
    table_class = tables.CostsTable
    filter_class = filters.CostFilter
    table_pagination = False
    create_url = reverse_lazy('costs-create')
    segment = 'costs'


class CostCreateView(CreateView, FormViewMixin):
    model = models.Costs
    template_name = 'generic/create.html'
    fields = '__all__'
    segment = 'costs'
    success_url = reverse_lazy('costs-list')


class CostUpdateView(UpdateView, FormViewMixin):
    model = models.Costs
    template_name = 'generic/detail.html'
    fields = '__all__'
    segment = 'costs'


class CostDeleteView(BaseDeleteView):
    model = models.Costs
    success_url = reverse_lazy('costs-list')
