from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.manyToOneRelation, name='m2o'),
    
]
