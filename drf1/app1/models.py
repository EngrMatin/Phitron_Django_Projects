from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class CourseInfo(models.Model):
    course_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, related_name='course', default=None)   ##
    course_name = models.CharField(max_length=50)
    marks = models.IntegerField()
    
    def __str__(self):
        return f"{self.course_name} : {self.marks}"

# # since the relationship is one to many or many to one, the above hashed line should be used within the "many" relationship class