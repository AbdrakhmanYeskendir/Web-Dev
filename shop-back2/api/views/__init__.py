# Переключатель уровней — меняй только эту строку!
# from .fbv import products_list, product_detail        # Level 2
# from .cbv import ProductListAPIView, ProductDetailAPIView  # Level 3
# from .mixins import ProductListAPIView, ProductDetailAPIView  # Level 4
from .generics import (  # Level 5 — активный
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView,
)