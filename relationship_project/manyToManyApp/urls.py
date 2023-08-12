from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.manyToManyRelation, name='m2m'),
    path('show/', views.showData, name='show'),
    
]
