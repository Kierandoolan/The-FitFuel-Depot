from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from products.models import Product
# Create your views here.


@login_required
def wishlist_view(request):
    """
    A view that displays users wishlist
    """
    wishlist_items_count = 0
    try:
        all_wishlist = wishlist.objects.filter(username=request.user.id)[0]
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