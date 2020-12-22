from django.shortcuts import render
from django.http import HttpResponse
from Staticov.models import workerlogin
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,'index.html')
def AdminDash(request):
    return render(request,'AdminDashBoard/index.html')
def contact(request):
    return render(request,'AdminDashBoard/contact.html')
def MainDashBoard(request):
    return render(request,'MainDashBoard/dashboardindex.html')

def test2(request):
    return render(request, 'test.html')

def test(request):
    if request.method == 'POST':
        saverecord = workerlogin()
        saverecord.days=request.POST.get('days')
        saverecord.numbers=request.POST.get('numbers')
        saverecord.positive=request.POST.get('positive')
        saverecord.save()
        return test2(request)
    else:
        return test2(request)

def testdata(request):
    if request.method == 'GET':
       data = workerlogin.objects.all().values()
       data_list = list(data)  # important: convert the QuerySet to a list object
       return JsonResponse(data_list, safe=False)






