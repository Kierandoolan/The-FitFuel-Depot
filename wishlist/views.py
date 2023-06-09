""" wishlist Views """
from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse
from products.models import Product
from .models import Wishlist

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
    """
    A view that will add a product item to wishlist
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        wishlist = get_object_or_404(Wishlist, username=request.user.id)
    except Http404:
        wishlist = Wishlist.objects.create(username=request.user)

    if product in wishlist.products.all():
        messages.info(request, 'The product is already in your wishlist!')
    else:
        wishlist.products.add(product)
        messages.info(request, 'Added the product to your wishlist')

    return redirect(reverse('product_detail', args=[item_id]))


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