from django.shortcuts import render, get_object_or_404
from .models import Products


# Create your views here.
def product_page(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    return render(request, 'products/product/product-page.html', {'product': product})


def product_list(request):
    products = Products.objects.all()
    return render(request, 'products/product-list.html', {'products': products})
