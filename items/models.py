from unicodedata import category
from django.db import models

# Create your models here.

class Categories(models.Model):
    categoryName = models.CharField(max_length=200)
    def __str__(self):
        return self.categoryName

class SubCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategoryName = models.CharField(max_length=200)
    def __str__(self):
        return self.subcategoryName

class Products(models.Model):
    productName = models.CharField(max_length=200)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    subCategory = models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    def __str__(self):
        return self.productName