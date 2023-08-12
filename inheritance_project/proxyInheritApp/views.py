from django.shortcuts import render

# Create your views here.
def proxyInherit(request):
    return render(request, 'proxyInheritApp/proxyInherit.html')