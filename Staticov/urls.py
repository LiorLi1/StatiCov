from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home'),
    path('index', views.index, name='index'),
    path('privacy', views.privacy, name='privacy'),
    path('rate', views.rate, name='rate'),
    path('AdminDash', views.AdminDash, name='AdminDash'),
    path('WorkerDash', views.WorkerDash, name='WorkerDash'),
    path('contact', views.contact, name='contact'),
    path('MainDashBoard', views.MainDashBoard, name='MainDashBoard'),
    path('registration', views.workerinsert, name='registration'),
    path('login', views.get_login_test, name='login'),
    path('datapatient', views.datapatient, name='datapatient'),
    path('addpatient', views.addpatient,name='addpatient'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('change_password_test', views.CHANGE_PASSWORD_TEST, name='change_password_test'),
    path('change_password',views.changepassword),
    path('patient_to_worker', views.patientworker),
    path('list_of_patients', views.new_patient),
    path('addworker', views.addworker),
    path('addworkerafterapproval', views.after_approuval_worker_insert),
    path('get_data_table', views.get_data_table),
    path('checksymptoms', views.check_symptomes),
]