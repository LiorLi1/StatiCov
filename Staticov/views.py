from django.shortcuts import render,redirect
from django.http import HttpResponse
from Staticov.models import Civilianform
from django.contrib import messages
import pandas as pd




# Create your views here.

def index(request):
    return render(request,'index.html')
def test(request):
    return render(request,'test.html')
def home(request):
    return render(request,'worker/about.html')




def Insertrecord(request):
 if request.method=='POST':
     saverecord=Civilianform()
     saverecord.name=request.POST.get('Name')
     saverecord.taz=request.POST.get('ID')
     saverecord.date=request.POST.get('DATE')
     saverecord.religion=request.POST.get('Religion')
     saverecord.place=request.POST.get('Place')
     saverecord.save()
     messages.success(request,'Record Saved Successfully...!')
     return home(request)
 else:
    return home(request)








