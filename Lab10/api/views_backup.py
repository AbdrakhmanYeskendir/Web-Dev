import json
from django.http import JsonResponse
from .models import Product, Category

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer

#lab 9

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail = True, methods = ['get'])
    def products(self, request, pk = None ):
        category = self.get_object()
        products = category.products.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, pk=None):
        product = self.get_object()
        if product.price > 500 and product.is_active:
            return Response(
                {'error': 'you cannot delete'},
                status=400
            )
        return super().destroy(request, pk)

    @action(detail=False, methods=['get'])
    def active(self, request):
        products = Product.objects.filter(is_active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def cheap(self, request):
        products = Product.objects.filter(price__lt=100000)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def expensive(self, request):
        products = Product.objects.filter(price__gt=50000)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)





#lab 8


# def product_list(request):
#     products = Product.objects.all()
#     data = []
#     for product in products:
#         data.append({
#             'id': product.id,
#             'name': product.name,
#             'price': product.price,
#             'description': product.description,
#             'count': product.count,
#             'is_active': product.is_active,
#             'category_id': product.category_id,
#         })
#     return JsonResponse(data, safe = False)
#
# def product_detail(request, id):
#     try:
#         product = Product.objects.get(id = id)
#         data = {
#             'id': product.id,
#             'name': product.name,
#         }
#         return JsonResponse(data)
#     except Product.DoesNotExist:
#         return JsonResponse({'error': 'Category not found'}, status = 404)
#
# def category_list(request):
#     category = Category.objects.all()
#     data = []
#     for category in Category:
#         data.append({
#             'id': category.id,
#             'name': category.id,
#         })
#         return JsonResponse(data, safe = False)
#
# def category_detail(request, id):
#     try:
#         category = Category.objects.get(id = id)
#         data = {
#             'id': category.id,
#             'name': category.name,
#         }
#         return JsonResponse(data)
#     except Category.DoesNotExist:
#         return JsonResponse({'error': 'Category not found'}, status = 404)
#
# def category_products(request, id):
#     try:
#         category = Category.objects.get(id = id)
#         products = category.products.all()
#         data = []
#         for product in products:
#             data.append({
#                 'id': product.id,
#                 'name': product.name,
#                 'price': product.price,
#                 'description': product.description,
#                 'count': product.count,
#                 'is_active': product.is_active,
#                 'category_id': product.category_id,
#             })
#         return JsonResponse(data, safe = False)
#     except Category.DoesNotExist:
#         return JsonResponse({'error': 'Category not found'}, status = 404)