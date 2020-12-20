from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name='index'),
    path('inscriptionform',views.inscription, name='inscriptionform'),
    path('home', views.home, name='about'),
    path('add_civilian',views.Insertrecord),
    path('homeciv',views.Homeinsert),
    path('worker_login',views.worker_login, name = 'worker-login'),
    path('registration',views.registration, name = 'registration'),
]
