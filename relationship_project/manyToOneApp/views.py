from django.shortcuts import render

# Create your views here.
def manyToOneRelation(request):
    return render(request, 'manyToOne.html')