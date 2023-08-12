"""
URL configuration for book app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('delete_session/', views.delete_session, name='delete_session'),
    path('get_cookies/', views.get_cookies, name='get_cookies'),
    path('del_cookie/', views.delete_cookies, name='delete_cookies'),
    path('add/', views.add_book, name='add_book'),
    path('show/', views.show_book, name='show_book'),
    path('edit/<int:id>', views.edit_book, name='edit_book'),
    path('delete/<int:id>', views.delete_book, name='delete_book'),
    
]
