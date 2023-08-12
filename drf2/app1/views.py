from django.shortcuts import render
from rest_framework import viewsets
from .models import ProductInfo, ReviewInfo
from .serializers import ProductSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import AdminOrReadOnly, ReviewerOrReadOnly

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [AdminOrReadOnly]
    queryset = ProductInfo.objects.all()
    serializer_class = ProductSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [ReviewerOrReadOnly]
    queryset = ReviewInfo.objects.all()
    serializer_class = ReviewSerializer