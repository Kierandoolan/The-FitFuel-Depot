from django.contrib import admin
from .models import Wishlist


class WishListAdmin(admin.ModelAdmin):
    """
    Admin class for the WishList model.
    """
    list_display = ('username',)
    search_fields = ('username',)
    list_filter = ('username',)


admin.site.register(Wishlist, WishListAdmin)