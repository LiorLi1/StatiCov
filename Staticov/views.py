from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')
def AdminDash(request):
    return render(request,'AdminDashBoard/index.html')
def contact(request):
    return render(request,'AdminDashBoard/contact.html')
def MainDash(request):
    return render(request,'MainDashBoard/MainDashBoardindex.html')


