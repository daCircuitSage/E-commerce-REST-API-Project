from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *



@api_view(['GEt'])
def product_list(request):
    products = Product.objects.filter(featured=True)
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail(request, slug):
    product = Product.objects.get(slug = slug)
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_detail(request,slug):
    category = Category.objects.get(slug=slug)
    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
def add_to_cart(request):
    cart_code = request.data.get('cart_code')
    product_id = request.data.get('product_id')

    cart, created = Cart.objects.get_or_create(cart_code = cart_code)
    product = Product.objects.get(id=product_id)

    cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cartitem.quantity = 1
    cartitem.save()
    
    serializer = CartSerializer(cart)
    return Response(serializer.data)