from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from products.models import Product, Comment

from .forms import CommentForm


def get_product(request, id=None):
    product = Product.objects.get(id=id)
    comments = Comment.objects.filter(product=id)

    comments_form = CommentForm()
    return render(request, 'products/show_product.html',
                  {'product': product,
                   'comments': comments,
                   'form': comments_form})


def get_list_of_products(request):
    products = Product.objects.all()

    return render(request, 'products/list_of_products.html',
                  {'products': products})


@login_required
@permission_required("products.add_comment", raise_exception=True)
def add_new_comment(request, id):
    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():
            user = request.user
            new_comment = form.save(commit=False)
            new_comment.author = user
            new_comment.product = Product.objects.get(id=id)

            new_comment.save()

        return redirect('product', id=id)

    else:
        return redirect('product', id=id)
