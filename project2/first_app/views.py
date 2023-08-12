from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return HttpResponse('''
                        <h1>This is the about page</h1>
                        <a href='/fa/courses/'>Courses</a>
                        <a href='/sa/contact/'>Contact</a>
                        <a href='/sa/feedback/'>Feedback</a>
                    
                        ''')

def courses(request):
    return HttpResponse('''
                        <h1>This is the courses page</h1>
                        <a href='/fa/about/'>About Us</a>
                        <a href='/sa/contact/'>Contact</a>
                        <a href='/sa/feedback/'>Feedback</a>
                        
                        ''')