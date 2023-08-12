from django.shortcuts import render

# Create your views here.
def multiInherit(request):
    return render(request, 'multiInheritApp/multiInherit.html')