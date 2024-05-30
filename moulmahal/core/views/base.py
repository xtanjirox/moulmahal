from django_tables2 import SingleTableView
from core import forms
from django.views import generic
from django.forms import modelform_factory
from django.db.models import F
from core import models
from django.db.models import Sum


class BaseListView(SingleTableView):
    template_name = "generic/list.html"
    segment = None
    filter_class = None
    show_only_filtered = None
    filter = None
    create_url = None
    get_stats = None

    def get_queryset(self):
        if self.filter_class:
            self.filter = self.filter_class(self.request.GET, queryset=super().get_queryset())
            if self.show_only_filtered and not self.request.GET:
                return self.model.objects.none()
            return self.filter.qs
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.filter_class:
            form = forms.FilterForm(self.filter.form)
            context.update({
                'filter': self.filter,
                'helper': form.helper
            })
        if self.get_stats:
            nb_product = self.model.objects.all().count()
            sum_product_quantity = sum(self.model.objects.all()
                                       .values_list('product_quantity', flat=True))
            stock_cost_price = sum(self.model.objects.all()
                                   .annotate(unit_stock_cost_price=F('product_quantity') * F('product_cost_price'))
                                   .values_list('unit_stock_cost_price', flat=True))
            total_sale_income = models.OrderItems.objects.aggregate(Sum('price'))

            context.update({
                'product_total_number': nb_product,
                'sum_product_quantity': sum_product_quantity,
                'stock_cost_price': stock_cost_price,
                'total_sale_income': total_sale_income.get('price__sum')
            })

        context.update({
            'segment': self.segment,
            'create_url': self.create_url,
        })
        print(context)
        return context


class FormViewMixin(generic.FormView):
    model = None
    fields = []
    attrs = {}
    widgets = {}
    exclude = None
    readonly_fields = []
    segment = None

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = modelform_factory(
                self.model, fields=self.fields, exclude=self.exclude, widgets=self.widgets
            )
        form = super().get_form(form_class=form_class)
        form.helper = forms.FormHelper()
        form.helper.form_tag = False
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'segment': self.segment
        })
        return context


class BaseDeleteView(generic.DeleteView):
    skip_confirmation = True

    def get(self, request, *args, **kwargs):
        if self.skip_confirmation:
            return self.delete(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)
