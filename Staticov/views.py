import json
from django.shortcuts import render
from django.http import HttpResponse
from Staticov.models import Admin,Civilian,Indexform,Registerform,Worker
from django.contrib import messages
import mysql.connector

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database="civilian"
)
cursor = db_connection.cursor()
print(db_connection)

#from .forms import InsertForm
# Create your views here.

def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'worker/about.html')
def inscription(request):
    return render(request,'inscriptionform.html')
def registrations(request):
    return render(request,'registration.html')
    
def workerinsert(request):
 if request.method=='POST':
     saverecord=Registerform()
     saverecord.taz=request.POST.get('taz')
     saverecord.name=request.POST.get('name')
     saverecord.password=request.POST.get('password')
     saverecord.type=request.POST.get('type')
     saverecord.save()
     messages.success(request,'Record Saved Successfully...!')
     return index(request)
 else:
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


def get_data_test(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM registerform")
    data = cursor.fetchall()
    for item in data:
        id,name,taz,password,type = item
        result['data'].append({
            'id':id,
            'name':name,
            'taz':taz,
            'password':password,
            'type':type,
        })
        print(result)
    return render(request,'table.html', result)



