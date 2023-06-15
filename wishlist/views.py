""" wishlist Views """
from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse
from products.models import Product
from .models import Wishlist


def error_403_view(request, exception):
    '''403 error view'''
    return render(request, '403.html', status=403)


def error_404_view(request, exception):
    '''404 error view'''
    return render(request, '404.html', status=404)


def error_500_view(request):
    """
    404 error view
    """
    return render(request, '500.html', status=500)


@login_required
def wishlist_view(request):
    """
    A view that displays users wishlist
    """
    wishlist_items_count = 0
    try:
        all_wishlist = Wishlist.objects.filter(username=request.user.id)[0]
    except IndexError:
        wishlist_items = None
    else:
        wishlist_items = all_wishlist.products.all()
        wishlist_items_count = all_wishlist.products.all().count()

    if not wishlist_items:
        messages.info(request, 'Your wishlist list is empty!')

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
        'wishlist_items_count': wishlist_items_count
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, item_id):
    """View to add a product to wishlist"""

    product = get_object_or_404(Products, pk=item_id)
    try:
        wishlist = get_object_or_404(Wishlist, username=request.user.id)
    except Http404:
        wishlist = Wishlist.objects.create(username=request.user)

    if product in wishlist.products.all():
        messages.info(request, 'The product is already in your wishlist!')
        messages.info(request, f'{product.name} is already in your \
            wishlist!')

    else:
        wishlist.products.add(product)
        messages.success(request, f'{product.name} successfully added \
            to your wishlist!')

    return redirect(reverse('product_details', args=[product.id]))


@login_required
def remove_from_wishlist(request, item_id, redirect_from):
    """
    A view that will add a product item to wishlist
    """
    product = get_object_or_404(Product, pk=item_id)
    wishlist = get_object_or_404(Wishlist, username=request.user.id)
    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.info(request, 'Removed the product '
                               'from your wishlist list')
    else:
        messages.error(request, 'That product is '
                                'not in your wishlist list!')
    if redirect_from == 'wishlist':
        redirect_url = reverse('wishlist')
    else:
        redirect_url = reverse('product_detail', args=[item_id])

    return redirect(redirect_url)