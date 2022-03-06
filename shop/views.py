from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product


# from django.db.models import Q


def product_list(request, category_slug=None):
    category = None
    search_product = request.GET.get('search', '')
    if search_product:
        products = Product.objects.filter(name__icontains=search_product, available=True)
    else:
        products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(Category__name=category).order_by('name')
    return render(request, 'shop/product/list.html',
                  {'category': category, 'products': products, 'search_product': search_product})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})


def about_me(request):
    return render(request, 'shop/about.html')
