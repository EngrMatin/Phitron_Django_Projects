from django.shortcuts import render

def home(request):
    return render(request, 'common_code/base.html') 