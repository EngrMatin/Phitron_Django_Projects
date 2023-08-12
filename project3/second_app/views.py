from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'index.html', context = {'author':'Phitron', 'age':19, 'marks':89})