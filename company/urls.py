from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('faq', views.faq, name='faq'),
    path('privatepolicy', views.privatepolicy, name='privatepolicy'),
    path('about-us/', views.about_us, name='about-us'),
]