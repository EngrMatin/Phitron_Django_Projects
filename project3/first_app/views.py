from django.shortcuts import render, redirect
from first_app.registration_form import RegistrationForm
from . import models
from .forms import StudentForm

# Create your views here.
def courses(request):
    return render(request, 'courses.html', {'courses':[
        {
            'id': 101,
            'course': 'C',
            'teacher': 'Rakib'
        },
        {
            'id': 102,
            'course': 'C++',
            'teacher': 'Sakib'
        },
        {
            'id': 103,
            'course': 'C#',
            'teacher': 'Jakib'
        }
    ]})

def practice(request):
    return render(request, 'practice.html', {'name':'Sakib', 'marks':86, 'age':22, 'list1':[2,4,39,5,3], 'blog': 'The Institution of Engineers, Bangladesh (IEB) is an institution for all the graduate engineers of Bangladesh.'})

def about(request):
    student = models.Student.objects.all()
    # print(student)
    return render(request, 'about.html', {'developer':'sadman sakib', 'student_info' : student})


def registration(request):
    if request.method == 'POST':
        # print(request.POST)
        print('Used method: POST')
        obj = RegistrationForm(request.POST, request.FILES)
        if obj.is_valid():
            # print('This form is valid')
            file = obj.cleaned_data['file']
            with open('./first_app/uploads/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                    
            print(obj.cleaned_data)
            # print('email : ', obj.cleaned_data['email'])
            # print('password : ', obj.cleaned_data['password'])
            # print('file : ', obj.cleaned_data['file'])
            
            # nam = obj.cleaned_data['name']
            # mob = obj.cleaned_data['mobile']
            # mail = obj.cleaned_data['email']
            
            
            # data = Students(name = nam, mobile = mob, email = mail, password = pas, confirm_password = con_pas, review = rev, age = ag, cgpa = gp, youtube = tube)
            # data.save()
            # return HttpResponseRedirect('/rev/ok')
    else:
        obj = RegistrationForm(auto_id=True, label_suffix=' : ')
        print('Used method: GET')
        
    return render(request, 'registration_form.html', {'form':obj} )

def delete_student(request, id):
    std = models.Student.objects.get(pk=id).delete()
    return redirect("about")

def student_registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            
            photo = form.cleaned_data['photo']
            with open('./first_app/uploads/' + photo.name, 'wb+') as destination:
                for chunk in photo.chunks():
                    destination.write(chunk)
                    
            print(form.cleaned_data)
            
            form.save()
    else:        
        form = StudentForm(auto_id=True, label_suffix=' : ')
        
    return render(request, 'student_reg_form.html', {'std_reg_form' : form} )