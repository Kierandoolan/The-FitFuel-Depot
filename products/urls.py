from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update_review/<pk>/', views.UpdateReviewView.as_view(),
         name='update_review'),
    path('submit_review/<int:product_id>/', views.submit_review,
         name='submit_review'),
    path('delete_review/<pk>/',
         views.ReviewDeleteView.as_view(),
         name='delete_review'),
]