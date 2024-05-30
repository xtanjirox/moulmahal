from django import forms

from . import models

from dynamic_forms import DynamicFormMixin, DynamicField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout


class FilterForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_tag = False
        fields = (Div(field, css_class='col-md-4') for field in args[0].fields.keys())
        self.helper.layout = Layout(
            Div(
                *fields,
                css_class='row'
            )
        )


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Clients
        fields = ['client_name', 'client_address', 'client_phone']
