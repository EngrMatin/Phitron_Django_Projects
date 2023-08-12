from django.shortcuts import render

# Create your views here.
def oneToOneRelation(request):
    return render(request, 'oneToOne.html')