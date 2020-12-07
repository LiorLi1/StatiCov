from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')
def test(request):
    return render(request,'test.html')
def home(request):
    return render(request,'worker/about.html')