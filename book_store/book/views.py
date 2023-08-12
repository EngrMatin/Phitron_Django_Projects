from django.shortcuts import render, redirect
from .forms import AddBookForm
from .models import AddBook
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.

def about(request):
    response = render(request, 'about.html')
    response.set_cookie('name','Sakib')
    # response.set_cookie('name','Rakib', max_age=60*10)
    response.set_cookie('name','Rakib', expires = datetime.utcnow()+timedelta(days=7))
    return response

def get_cookies(request):
    name = request.COOKIES.get('name')
    return render(request, 'get_cookies.html', {'name': name})

def delete_cookies(request):
    response = render(request, 'delete_cookies.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    data = {
        'name' : 'Sakib',
        'age' : 25,
        'language' : 'Bangla'
    }
    # print(request.session.get_session_cookie_age())     
    # print(request.session.get_expiry_date())
    request.session.update(data)                      # SESSION_COOKIE_AGE must be set in settings.py
    return render(request, 'about.html')   

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name')
        age = request.session.get('age')
        request.session.modified = True
        return render(request, 'get_session.html', {'name': name, 'age': age}) 
    else:
        return HttpResponse('Session expired')

def delete_session(request):
    request.session.flush()
    return render(request, 'delete_cookies.html')   


def add_book(request):
    if request.method == 'POST':
        obj = AddBookForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            obj.save()
            return redirect("show_book")
    else:
        obj = AddBookForm()        
            
    return render(request, 'add_book.html', {'form':obj})

def show_book(request):
    book = AddBook.objects.all()
    return render(request, 'show_book.html', {'book_list':book})

def edit_book(request, id):
    book = AddBook.objects.get(pk=id)
    form = AddBookForm(instance=book)
    if request.method == 'POST':
        obj = AddBookForm(request.POST, instance = book)
        if obj.is_valid():
            print(obj.cleaned_data)
            obj.save()
            return redirect("show_book")
    return render(request, 'add_book.html', {'form':form})

def delete_book(request, id):
    book = AddBook.objects.get(pk=id).delete()
    return redirect("show_book")