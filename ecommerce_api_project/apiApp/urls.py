from django.urls import path
from .views import *

urlpatterns = [
    path('product_list', product_list, name='product_list'),
    path('product/<slug:slug>', product_detail, name='product_detail'),
    path('category_list', category_list, name='category_list'),
    path('category/<slug:slug>', category_detail, name='category_detail'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('update_cartitem_quantity/', update_cartitem_quantity, name='update_cartitem_quantity'),
    path('add_review/', add_review, name='add_review'),
    path('update_review/<int:pk>/', update_review, name='update_review'),
    path('delete_reivew/<int:pk>/', delete_review, name='delete_review'),
]
