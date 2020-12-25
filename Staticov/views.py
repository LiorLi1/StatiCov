from django.shortcuts import render
from django.http import HttpResponse
from Staticov.models import Civilianform
from Staticov.models import index_form
from Staticov.models import worker_register
from Staticov.models import login_form
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import AuthenticationForm


#from .forms import InsertForm
# Create your views here.

def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'test.html')
def inscription(request):
    return render(request,'inscriptionform.html')
def registrations(request):
    return render(request,'registrationform.html')
    
def workerinsert(request):
 if request.method=='POST':
     saverecord=worker_register()
     saverecord.userid=request.POST.get('userid')
     saverecord.name=request.POST.get('name')
     saverecord.password=request.POST.get('password')
     saverecord.save()
     messages.success(request,'Record Saved Successfully...!')
     return index(request)
 else:
     return registrations(request)

def loginform(request):
    if request.method=='GET':
        data=login_form.objets.all().values
        form=login_form(data=request.POST)
        if form.is_valid():
            return index(request)
    else :
        return registrations(request)
    

def indexcontact(request):
 if request.method=='POST':
     saverecord=index_form()
     saverecord.name=request.POST.get('name')
     saverecord.taz=request.POST.get('taz')
     saverecord.telephone=request.POST.get('telephone')
     saverecord.symptomes=request.POST.get('symptomes')
     saverecord.save()
     messages.success(request,'Record Saved Successfully...!')
     return registrations(request)
 else:
     return index(request)


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





