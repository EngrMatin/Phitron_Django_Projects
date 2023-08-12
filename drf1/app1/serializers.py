from rest_framework import serializers
from .models import CourseInfo, StudentInfo


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseInfo
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    # course = CourseSerializers(many=True, read_only=True)   ## "course" has come from "related_name" attribute in the models.py
    # course = serializers.StringRelatedField(many=True)   ## To view {course_name} : {marks}, copy code from  https://www.django-rest-framework.org/api-guide/relations/
    course = serializers.HyperlinkedRelatedField(        ## To view hyperlink, copy code from https://www.django-rest-framework.org/api-guide/relations/
        many=True,
        read_only=True,
        view_name='course_details'
    )
      
    class Meta:
        model = StudentInfo
        fields = '__all__'
        
# # since the relationship is one to many or many to one, the above hashed line should be used within the "one" relationship class
## 
        

        
