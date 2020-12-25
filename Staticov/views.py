import json
from django.shortcuts import render
from django.http import HttpResponse
from Staticov.models import Civilianform
from Staticov.models import index_form
from Staticov.models import worker_register
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
    return render(request,'registrationform.html')
    
def workerinsert(request):
 if request.method=='POST':
     saverecord=worker_register()
     saverecord.userid=request.POST.get('userid')
     saverecord.name=request.POST.get('name')
     saverecord.password=request.POST.get('password')
     saverecord.save()
     messages.success(request,'Record Saved Successfully...!')
     raw_password = saverecord.password
     user = authenticate(username=saverecord.userid, password= raw_password)
     login(request, user)
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
    result = []
    cursor.execute("SELECT * FROM civilianform")
    data = cursor.fetchall()
    for item in data:
        print(item)
        name, user_id, date, phone, age, place = item
        result.append({
            'name': name,
            'user_id': user_id,
            'date': str(date),
            'phone': phone,
            'age': age,
            'place': place
        })
    return HttpResponse(json.dumps(result), content_type="application/json")



