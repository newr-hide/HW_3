from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_data = Phone.objects.all()

    # Получить текущий параметр сортировки
    sort_param = request.GET.get('sort')
    if not sort_param:
        sort_param = 'name'

    # Применить фильтр к данным
    if sort_param == 'name':
        phone_data = phone_data.order_by('name')
    elif sort_param == 'min_price':
        phone_data = phone_data.order_by('price')
    else: #sort_param == 'max_price'
        phone_data = phone_data.order_by('-price')

    context = {
        'phones': phone_data,
        'sort_by': sort_param
    }
    return render(request, template, context)
# def show_catalog(request):
#     template = 'catalog.html'
#     phone_data = Phone.objects.all()
#
#     context = {
#         'phones' : phone_data
#     }
#     return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_data = Phone.objects.get(slug=slug)


    context = {
        'phone': phone_data
        }
    return render(request, template, context)

