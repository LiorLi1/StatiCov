from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from Staticov.models import AdminModel
from Staticov.models import Patientworker
from Staticov.models import CivilianModel
from Staticov.models import IndexFormModel
from Staticov.models import RegisterFormModel
from Staticov.models import WorkersModel
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
    #regular registration before 
    return render(request,'registrationform.html')
def add_patient(request):
    #worker page -> to insert new patient to the form_civilian_db
    return render(request,'WorkerDashBoard/addpatient.html')
def privacy(request):
    return render(request,'privacy_policy.html')
def changepassword(request):
    #page to change password to all users
    return render(request, 'changepassword.html')
def patientworker(request):
    #page to assign new patients to workers
    return render(request,'patienttoworker.html')
def addworker(request):
    return render(request,'AdminDashBoard/addworker.html')

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
    return HttpResponse(JSON.dumps(result), content_type="application/json")

def CHANGE_PASSWORD_TEST(request):
    if request.method=='POST':
        useridtest=request.POST.get('taz')
        passwordcurrentpassword=request.POST.get('current_password')
        passwordtest=request.POST.get('password')
        result = []
        cursor.execute("SELECT * FROM `registerform`")
        data = cursor.fetchall()    
        for item in data:
            ID,name,taz,password,type = item
            if taz==useridtest and password == passwordcurrentpassword :
                cursor.execute("UPDATE `registerform` SET `password` = '%s' WHERE `registerform`.`ID` = '%s';"%(passwordtest,ID))
                db_connection.commit()
                return index(request)
        else:
            messages.error(request,'הפרטים שהוזנו לא נמצאים במערכת')   
            return changepassword(request)

def new_patient(request):
    if request.method=='POST':
        saverecord=Patientworker()
        saverecord.telephone=request.POST.get('telephone')
        saverecord.taz=request.POST.get('taz')
        saverecord.workerid=request.POST.get('workerid')
        saverecord.save()
        messages.success(request,'Record Saved Successfully...!')
        return render(request,'patienttoworker.html')
    else:
        messages.error(request,'Error')
        return render(request,'patienttoworker.html')

def datapatient(request):
    if request.method == 'GET':
        cursor.execute("SELECT * FROM formcivilian")
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

def after_approuval_worker_insert(request):
 if request.method=='POST':
     saverecord=WorkersModel()
     saverecord.taz=request.POST.get('taz')
     saverecord.name=request.POST.get('name')
     saverecord.password=request.POST.get('password')
     saverecord.Type=request.POST.get('Type')
     saverecord.save()
     messages.success(request,'הנתונים נשמרו בהצלחה!')
     return addworker(request)
 else:
     return addworker(request)

def get_data_table(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM registerform")
    data = cursor.fetchall()
    for item in data:
        ID,name,taz,password,type = item
        result['data'].append({
            'id':ID,
            'name':name,
            'taz':taz,
            'password':password,
            'type':type,
        })
        print(result)
    return render(request,'AdminDashBoard/addworker.html', result)

    
            










