from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name='index'),
    path('test', views.test, name='page'),
    path('home', views.home, name='about'),
    path('add_civilian',views.Insertrecord)
]
