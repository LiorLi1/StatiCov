from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from Staticov.models import AdminModel
from Staticov.models import CivilianModel
from Staticov.models import IndexFormModel
from Staticov.models import RegisterFormModel
from Staticov.models import WorkerModel
from django.contrib import messages
import mysql.connector
# Create your views here.

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database="civilian"
)
cursor = db_connection.cursor()
print(db_connection)

def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
def rate(request):
    return render(request,'rating.html')
def AdminDash(request):
    return render(request,'AdminDashBoard/index.html')
def WorkerDash(request):
    return render(request,'WorkerDashBoard/index.html')
def contact(request):
    return render(request,'AdminDashBoard/contact.html')
def MainDashBoard(request):
    return render(request,'MainDashBoard/dashboardindex.html')
def registration(request):
    return render(request,'registrationform.html')
def add_patient(request):
    return render(request,'WorkerDashBoard/addpatient.html')
def privacy(request):
    return render(request,'privacy_policy.html')

def workerinsert(request):
 if request.method=='POST':
     saverecord=RegisterFormModel()
     saverecord.taz=request.POST.get('taz')
     saverecord.name=request.POST.get('name')
     saverecord.password=request.POST.get('password')
     saverecord.Type=request.POST.get('Type')
     saverecord.save()
     messages.success(request,'הנתונים נשמרו בהצלחה!')
     return registration(request)
 else:
     return registration(request)


def indexcontact(request):
 if request.method=='POST':
     saverecord=IndexFormModel()
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
       ID,name,taz,password,type = item
    if useridtest==taz and passwordtest == password and type == 'מנהל':
        return AdminDash(request)
    elif useridtest==taz and passwordtest == password and type == 'עובד מדינה':
        return WorkerDash(request)
    elif useridtest==taz and passwordtest == password and type == 'אזרח':
        return index(request) 

    messages.error(request,'הפרטים שהוזנו לא נמצאים במערכת')   
    return registration(request) 

def get_data_test(request):
    result = []
    cursor.execute("SELECT * FROM `worker-register`")
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
        if useridtest==userid and passwordtest == password:
                print('lalalalal')
    return HttpResponse(json.dumps(result), content_type="application/json")

def datapatient(request):
    if request.method == 'GET':
        cursor.execute("SELECT * FROM `formcivilian`")
        data = cursor.fetchall()
        data_list = list(data)
        return JsonResponse(data_list, safe=False)

def addpatient(request):
    if request.method=='POST':
        saverecord=CivilianModel()
        saverecord.taz=request.POST.get('taz')
        saverecord.age=request.POST.get('age')
        saverecord.place=request.POST.get('place')
        saverecord.date=request.POST.get('date')
        saverecord.religion=request.POST.get('religion')
        saverecord.save()
        messages.success(request,'הנתונים נשמרו בהצלחה!')
        return WorkerDash(request)
    else:
        return add_patient(request)

    
            










