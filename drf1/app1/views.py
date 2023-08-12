from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentInfo, CourseInfo
from .serializers import StudentSerializers, CourseSerializers

## 3. To perform all 4 CRUD operation by writing only ONE class, copy code from https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
from rest_framework.viewsets import ModelViewSet

class StudentViewSet(ModelViewSet):
# class StudentViewSet(ReadOnlyModelViewSet):     ## To make it read-only
    queryset = StudentInfo.objects.all()
    serializer_class = StudentSerializers



## 2. To perform 4 CRUD operation by writing TWO class, copy code from https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-generic-class-based-views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# class StudentListCreateView(ListCreateAPIView):
#     queryset = StudentInfo.objects.all()
#     serializer_class = StudentSerializers

# class StudentRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
#     queryset = StudentInfo.objects.all()
#     serializer_class = StudentSerializers


class CourseListCreateView(ListCreateAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseSerializers

class CourseRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseSerializers





### 1. To perform 4 CRUD operation by writing MULTIPLE class, copy code from https://www.django-rest-framework.org/tutorial/3-class-based-views/
# class StudentView(APIView):
#     def get(self, request, format=None):
#         student_data = StudentInfo.objects.all()
#         serializer = StudentSerializers(student_data, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# class StudentDetailView(APIView):
#     def get(self, request, pk):
#         obj = StudentInfo.objects.get(pk=pk)
#         serializer = StudentSerializers(obj)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         obj = StudentInfo.objects.get(pk=pk)
#         serializer = StudentSerializers(obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         obj = StudentInfo.objects.get(pk=pk)
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
