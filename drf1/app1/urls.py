from django.urls import path, include
from . import views

## copy code from https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)


urlpatterns = [
    # path('', views.StudentView.as_view()),
    # path('<int:pk>/', views.StudentDetailView.as_view()),
    # path('', views.StudentListCreateView.as_view()),
    # path('<int:pk>/', views.StudentRetrieveUpdateView.as_view()),
    path('course/', views.CourseListCreateView.as_view()),
    path('course/<int:pk>/', views.CourseRetrieveUpdateView.as_view(), name="course_details"),
    path('', include(router.urls)),
    
]
