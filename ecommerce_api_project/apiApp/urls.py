from django.urls import path
from .views import *

urlpatterns = [
    path('product_list', product_list, name='product_list'),
    path('product/<slug:slug>', product_detail, name='product_detail'),
    path('category_list', category_list, name='category_list'),
    path('category/<slug:slug>', category_detail, name='category_detail'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
]
