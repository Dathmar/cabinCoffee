from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.http import JsonResponse
from .models import Cart
from products.models import Products
import json

"""
    a cart is saved to a user session. A cart is a list of dictionary
"""


# Create your views here.
@require_POST
def add_to_cart(request):
    """
    add an item to the cart.  the body of the request will be a JSON object like
    {
        'product_id': 1,
        'quantity': 1,
        'override_quantity': False
    }
    :return: Return a http status
    """

    body = json.loads(request.body)

    cart = Cart(request)
    product = Products.objects.get(id=body.get('product_id'))
    quantity = body.get('quantity')
    override_quantity = body.get('override_quantity', False)
    if not product:
        return JsonResponse(status=404)
    else:
        cart.add(product, quantity, override_quantity)
        return JsonResponse(data={}, status=200)


@require_POST
def remove_from_cart(request):
    """
    remove an item to the cart.  the body of the request will be a JSON object like
    {
        'product_id': 1,
    }
    :return: Return a http status
    """

    body = json.loads(request.body)

    cart = Cart(request)
    product = Products.objects.get(id=body.get('product_id'))

    if not product:
        return JsonResponse(status=404)
    else:
        cart.remove(product)
        return JsonResponse(data={}, status=200)
