from django.shortcuts import render

# Create your views here.
def abstract(request):
    return render(request, 'abstractClassApp/abstract.html')
