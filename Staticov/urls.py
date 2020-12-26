from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name='index'),
    path('AdminDash', views.AdminDash, name='AdminDash'),
    path('contact', views.contact, name='contact'),
    path('MainDashBoard', views.MainDashBoard, name='MainDashBoard'),
    path('registration', views.workerinsert, name='registration'),
    path('login', views.get_login_test, name='login'),
]