from rest_framework import serializers 
from items.models import Products
 
 
class ItemSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Products
        fields = ('id',
                  'productName',
                  'category',
                  'subCategory')