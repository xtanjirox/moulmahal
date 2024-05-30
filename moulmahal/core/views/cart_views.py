from django.shortcuts import render

from core import forms


def cart_views(request):
    print(request.POST)
    if request.POST.get('client_name') and request.POST.get('client_phone'):
        client_form = forms.ClientForm(request.POST or None)
    else:
        client_form = forms.ClientForm()

    context = {
        'form': client_form,
    }
    if client_form.is_valid():
        print("valid", (request.POST.get('client_name')))

    return render(request, 'cart_views.html', context)
