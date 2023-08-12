from django.db import models

# Create your models here.
class FriendModel(models.Model):
    school = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    attendance = models.BooleanField()
    cw = models.BooleanField()
    hw = models.BooleanField()
    
class MeModel(FriendModel):
    class Meta:
        proxy = True
        ordering = ['id']
    

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

class Employee(Person):
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()

    # class Meta:
    #     proxy = True

class Manager(Employee):
    class Meta:
        proxy = True

    def get_employees(self):
        return Employee.objects.filter(job_title='Manager', salary__gt=self.salary)

# In the above example, Employee is a concrete model that inherits from Person. 
# Manager is a proxy model that inherits from Employee. 
# Manager does not add any new fields, but it does add a new method, get_employees(), 
# that returns all the employees with the job title of "Manager" and 
# a higher salary than the manager.