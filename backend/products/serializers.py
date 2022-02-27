import re
from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # if you want to see get_discount instance method from models as "discount"
    my_discount = serializers.SerializerMethodField(read_only= True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_my_discount(self, obj):
        # print(obj.id)
        # obj.user -> user.username
        # obj.category -> user.category
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
        
        