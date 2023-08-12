from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contact(request):
    return HttpResponse('''
                        <h1>This is the contact page</h1>
                        <a href='/fa/about/'>About Us</a>
                        <a href='/fa/courses/'>Courses</a>
                        <a href='/sa/feedback/'>Feedback</a>
                        ''')

def feedback(request):
    return HttpResponse('''
                        <h1>This is the feedback page</h1>
                        <a href='/fa/about/'>About Us</a>
                        <a href='/fa/courses/'>Courses</a>
                        <a href='/sa/contact/'>Contact</a>
                        ''')