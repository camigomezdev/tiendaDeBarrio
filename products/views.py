from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products.models import Product

# from .forms import CommentForm, LikesForm


def get_product(request, id=None):
    product = Product.objects.get(id=id)
    return render(request, 'products/show_product.html', {'product': product})


def get_list_of_products(request):
    products = Product.objects.all()
    return render(request, 'products/list_of_products.html', {'products': products})
