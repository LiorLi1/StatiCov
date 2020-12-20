from django.shortcuts import render,redirect
from django.http import HttpResponse
from Staticov.models import Civilianform
from django.contrib import messages
import pandas as pd




# Create your views here.

def index(request):
    return render(request,'index.html')
def test(request):
    
    return render(request,'test.html',{'df':data})
def home(request):
    return render(request,'worker/about.html')




def Insertrecord(request):
 if request.method=='POST':
     saverecord=Civilianform()
     saverecord.name=request.POST.get('Name')
     saverecord.ID=request.POST.get('ID')
     saverecord.telephone=request.POST.get('telephone')
     saverecord.date=request.POST.get('DATE')
     saverecord.religion=request.POST.get('Religion')
     saverecord.age=request.POST.get('age')
     saverecord.place=request.POST.get('Place')
     saverecord.email=request.POST.get('email')
     saverecord.save()
     messages.success(request,'Record Saved Successfully...!')
     return home(request)
 else:
    return home(request)








