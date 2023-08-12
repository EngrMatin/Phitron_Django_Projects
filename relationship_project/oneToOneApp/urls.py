from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.oneToOneRelation, name='o2o'),
    
]
