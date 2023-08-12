from django.shortcuts import render
from manyToManyApp.forms import StudentForm
from .models import Student, Teacher

# Create your views here.
def manyToManyRelation(request):
    if request.method == 'POST':
        obj = StudentForm(request.POST)
        if obj.is_valid():
            obj.save()
            # return redirect("show")
    else:
        obj = StudentForm()        
            
    return render(request, 'manyToMany.html', {'form':obj})


def showData(request):
    # student list for one teacher
    teacher = Teacher.objects.get(name='Teacher2')
    student_list = teacher.student.all()   # s of Student should be lower case
    for x in student_list:
        print(x.name, x.roll, x.class_name)
        
    # teacher list for one student
    student = Student.objects.get(name='Student2')
    teacher_list = student.teachers.all()   # t of Teacher should be lower case
    for x in teacher_list:
        print(f'{x.name} {x.subject} {x.mobile}')
        
    return render(request, 'show_data.html')



#     if    student = models.ManyToManyField(Student, related_name='teachers')     in model
#           teacher_list = student.teachers.all()   

#     if    student = models.ManyToManyField(Student)     in model
#           teacher_list = student.teacher_set.all()   

        

