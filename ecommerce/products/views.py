from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def from_App(request):
    return HttpResponse("This is response from App")


def sec_fcn(request):
    return HttpResponse("This is second")


def show_index_page(request):
    return render(request, 'products/index.html')


def second_function(request):
    return render(request, 'products/second.html')


def new_file(request):
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'products/new.html', context)
