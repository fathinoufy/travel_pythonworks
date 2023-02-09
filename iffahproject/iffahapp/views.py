from django.http import HttpResponse
from django.shortcuts import render
from.models import Place
from.models import Team

# Create your views here.
def add(request):
    obj = Place.objects.all()
    ans=Team.objects.all()
    return render(request,'index.html',{'result':obj,'result2':ans})

def addition(request):
    return render(request,"index.html")
