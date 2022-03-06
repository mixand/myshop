from cart.cart import Cart
from .models import Category


def general_options(request):
    return {'categories': Category.objects.all(), 'cart': Cart(request)}
