from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_data = Phone.objects.all()

    context = {
        'phones' : phone_data
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_data = Phone.objects.all()
    for phone in phone_data:

        context = {
            'phone': phone
        }
    return render(request, template, context)

