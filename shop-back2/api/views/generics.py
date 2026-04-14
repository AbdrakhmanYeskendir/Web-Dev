from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Product, Category
from ..serializers import ProductSerializer, CategorySerializer


# Product views
class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'


# Category views
class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'


# Custom view: все продукты конкретной категории
class CategoryProductsAPIView(APIView):

    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Not found'}, status=404)
        products = category.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)