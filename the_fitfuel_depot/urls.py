
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('company/', include('company.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# override the standard error handlers
handler403 = 'the_fitfuel_depot.views.handler403'
handler404 = 'the_fitfuel_depot.views.handler404'
handler405 = 'the_fitfuel_depot.views.handler405'
handler500 = 'the_fitfuel_depot.views.handler500'
