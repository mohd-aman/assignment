from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allcategories', views.getAllCategories, name='allCategory'),
    path('<str:categories>/allsubcategory', views.getAllSubcategories, name='categories'),
    path('<str:categories>/getcategoryproduct', views.getAllProductsFromCategories, name='getAllProductsFromCategories'),
    path('<str:subcategories>/getsubcategoryproduct', views.getAllProductsFromSubcategories, name='getAllProductsFromSubcategories'),
    path('addProduct', csrf_exempt(views.addProduct), name="addProduct"),
]