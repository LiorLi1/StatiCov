from django.shortcuts import render
from django.http import HttpResponse
from Staticov.models import Civilianform
from Staticov.models import contactmainpage
from Staticov.models import worker_register
from django.contrib import messages

#from .forms import InsertForm
# Create your views here.

def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'worker/about.html')
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

def Homeinsert(request):
 if request.method=='POST':
     saverecord=contactmainpage()
     saverecord.name=request.POST.get('Name')
     saverecord.email=request.POST.get('email')
     saverecord.telephone=request.POST.get('telephone')
     saverecord.religion=request.POST.get('symptomes')
     saverecord.age=request.POST.get('age')
     saverecord.save()
     messages.success(request,'Record Saved Successfully...!')
     return index(request)
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





