from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name='index'),
    path('home', views.home, name='about'),
    path('registration',views.workerinsert),
    path('index_form',views.indexcontact),
    path('login', views.get_login_test),
    path('tamere', views.CHANGE_PASSWORD_TEST),
    path('passpage',views.testpassword),
    path('get_data_table', views.get_data_table),
   ]
