from rest_framework import serializers, viewsets
from .models import ProductInfo, ReviewInfo


class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model = ProductInfo
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):      
    class Meta:
        model = ReviewInfo
        fields = '__all__'
        
 
        

        
