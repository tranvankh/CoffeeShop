from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:coffee_id>/', views.add_to_cart, name='add_to_cart'),
]