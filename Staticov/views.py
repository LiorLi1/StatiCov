import json
from django.shortcuts import render
from django.http import HttpResponse
from Staticov.models import IndexModel
from Staticov.models import RegisterFormModel
from Staticov.models import AdminModel
from Staticov.models import WorkerModel
from Staticov.models import CivilianModel
from django.contrib import messages
import mysql.connector


db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database="civilian"
)
cursor = db_connection.cursor()
print(db_connection)

def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'addpatiente.html')
def registrations(request):
    return render(request,'registrationform.html')
    
def workerinsert(request):
 if request.method=='POST':
     saverecord=RegisterFormModel()
     saverecord.taz=request.POST.get('taz')
     saverecord.name=request.POST.get('name')
     saverecord.password=request.POST.get('password')
     saverecord.Type=request.POST.get('Type')
     saverecord.save()
     messages.success(request,'Record Saved Successfully...!')
     return index(request)
 else:
     return registrations(request)


def indexcontact(request):
 if request.method=='POST':
     saverecord=IndexModel()
     saverecord.name=request.POST.get('name')
     saverecord.taz=request.POST.get('taz')
     saverecord.telephone=request.POST.get('telephone')
     saverecord.symptomes=request.POST.get('symptomes')
     saverecord.save()
     messages.success(request,'Record Saved Successfully...!')
     return index(request)
 else:
     return index(request)


def get_login_test(request):
    result = []
    cursor.execute("SELECT * FROM `registerform`")
    data = cursor.fetchall()
    if request.method=='POST':
         useridtest=request.POST.get('taz')
         passwordtest=request.POST.get('password')
    for item in data:
        ID,name,taz,password,Type = item
        if useridtest==taz and passwordtest == password:
            return index(request)
    messages.error(request,'Please provide valid credentials')   
    return registrations(request)
      

def get_data_test(request):
    result = []
    cursor.execute("SELECT * FROM civilianform")
    data = cursor.fetchall()
    if request.method=='POST':
         useridtest=request.POST.get('userid')
         passwordtest=request.POST.get('password')
    for item in data:
        print(item)
        print(useridtest)
        print(passwordtest)
        ID,userid,name,password = item
        result.append({
            'userid': userid,
            'name': name,
            'password': password,
            'useridtest' : useridtest,
            'passwordtest' : passwordtest,     

        })
    return HttpResponse(json.dumps(result), content_type="application/json")