from django.db import models
from django.conf import settings
from products.models import Products
from decimal import Decimal


# Create your models here.
class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the card and get the products from the database
        """
        product_ids = self.cart.keys()
        products = Products.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        count all items in the cart
        :return: total items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        sum the total prices of all items in cart
        :return: total value of all items in cart
        """
        return sum(Decimal(item['price'] * item['quantity'] for item in self.cart.values()))

    def clear(self):
        # remove the cart from the session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def add(self, product, quantity=1, override_quantity=False):
        """
        add an item to the cart
        :param product: the product that should be added to the cart
        :param quantity: the number of the product that should be added to the cart
        :param override_quantity: if the quantity is additive then False if it's the total number of items True
        :return: No return
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        """
        Removes a product from the cart
        :param product: the product that should be removed from the cart
        :return: No return
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True
