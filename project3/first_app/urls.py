"""
URL configuration for first_app app.

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
    path('courses/', views.courses, name='courses'),
    path('practice/', views.practice, name='practice'),
    path('about/', views.about, name='about'),
    path('reg/', views.registration, name='reg_form'),
    path('delete/<int:id>', views.delete_student, name='delete_student'),
    path('std/reg/', views.student_registration, name='std_reg'),
    
]
