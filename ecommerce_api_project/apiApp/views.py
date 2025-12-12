from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import get_user_model



User = get_user_model()



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


@api_view(['PUT'])
def update_cartitem_quantity(request):
    cartitem_id = request.data.get('item_id')
    quantity = request.data.get('quantity')

    quantity = int(quantity)

    cartitem = CartItem.objects.get(id = cartitem_id)
    cartitem.quantity = quantity
    cartitem.save()

    serializer = CartItemSerializer(cartitem)
    return Response({'data':serializer.data, 'msg':'Cartitem update successfully'})



#--------------------------add review

@api_view(['POST'])
def add_review(request):
    
    product_id = request.data.get('product_id')
    email = request.data.get('email')
    rating = request.data.get('rating')
    review_text = request.data.get('review')

    product = Product.objects.get(id=product_id)
    user = User.objects.get(email=email)

    if Review.objects.filter(product=product, user=user).exists():
        return Response('User cannot drop more then one review for this product')

    review = Review.objects.create(product=product, user=user, rating=rating, review=review_text)
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_review(request, pk):
    review = Review.objects.get(id=pk)

    
    rating = request.data.get('rating')
    review_text = request.data.get('review')

    if rating is None:
        return Response({"error": "rating is required"}, status=400)

    review.rating = rating
    review.review = review_text
    review.save()

    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_review(request,pk):
    try:
        review = Review.objects.get(id=pk)
    except Review.DoesNotExist:
        return Response({'error':'Review not found'}, status=status.HTTP_404_NOT_FOUND)
    review.delete()
    return Response('Review deleted successfully', status=status.HTTP_200_OK)


