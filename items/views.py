import json
from operator import length_hint
from socket import CAN_RAW
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from items.serializer import ItemSerializer
from rest_framework import status
from .models import Categories, SubCategories, Products


def index(request):
    return render(request,'index.html')

def getAllCategories(request):
    all_categories = Categories.objects.all()
    allList =[]
    for i in all_categories:
        allList.append(i)
        allList.append("$")
    return HttpResponse(allList)

def getAllSubcategories(request,categories):
    category_id = get_object_or_404(Categories, categoryName=categories)
    all_subcategories = SubCategories.objects.filter(category = category_id.id)
    allList =[]
    for i in all_subcategories:
        allList.append(i)
        allList.append("$")
    return HttpResponse(allList)

def getAllProductsFromCategories(request,categories):
    category_id = get_object_or_404(Categories, categoryName=categories)
    all_products = Products.objects.filter(category = category_id.id)
    allList =[]
    for i in all_products:
        allList.append(i)
        allList.append("$")
    return HttpResponse(allList)

def getAllProductsFromSubcategories(request,subcategories):
    subcategory_id = get_object_or_404(SubCategories, subcategoryName=subcategories)
    all_products = Products.objects.filter(subCategory = subcategory_id.id)
    allList =[]
    for i in all_products:
        allList.append(i)
        allList.append("$")
    return HttpResponse(allList)

def addProduct(request):
    product_data = JSONParser().parse(request)
    print(product_data)
    category_id = get_object_or_404(Categories, categoryName=product_data['category'])
    subcategory_id = get_object_or_404(SubCategories, subcategoryName=product_data['subCategory'])
    data={"productName":product_data['productName'],"category":category_id.id,"subCategory":subcategory_id.id}
    print(data)
    product_serializer = ItemSerializer(data=data)
    if product_serializer.is_valid():
        product_serializer.save()
        return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
