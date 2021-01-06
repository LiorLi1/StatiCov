from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('index', views.index, name='index'),
    path('indexcontact', views.indexcontact, name='indexcontact'),
    path('privacy', views.privacy, name='privacy'),
    path('rate', views.rate, name='rate'),
    path('AdminDash', views.AdminDash, name='AdminDash'),
    path('WorkerDash', views.WorkerDash, name='WorkerDash'),
    path('contact', views.contact, name='contact'),
    path('MainDashBoard', views.MainDashBoard, name='MainDashBoard'),
    path('registration_before_admin_approval', views.registration_before_admin_approval),
    path('login', views.login, name='login'),
    path('datapatient', views.datapatient, name='datapatient'),
    path('addpatient', views.addpatient,name='addpatient'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('change_password', views.CHANGE_PASSWORD, name='change_password'),
    path('change_password',views.changepassword),
    path('after_approuval_worker_insert', views.after_approuval_worker_insert),
    path('get_new_workers_table', views.get_new_workers_table),
    path('checksymptoms', views.check_symptomes),
    path('symptomesformcheck', views.symptomesformcheck),
    path('Deleteworker', views.Deleteworker),
    path('workerdelete', views.workerdelete),
    path('get_new_workers_table', views.get_new_workers_table),
    path('get_new_positiv_table', views.get_new_positiv_table),
    path('assign_patient', views.assign_patient),
    path('get_new_patient_table', views.get_new_patient_table),
    
       
]