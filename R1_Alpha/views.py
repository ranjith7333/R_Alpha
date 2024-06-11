from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Pages 

def home(request):
    return render(request,"home.html")
    
def index(request):
    return render(request,"index.html")
    
def clocking(request):
    EMPID=request.POST ['EMP ID']   
    WONO=request.POST ['WO#']  
    CATAGORY=request.POST ['CATAGORY']  
    HOURS=request.POST ['HOURS']  
    DESCRIPTION=request.POST ['DESCRIPTION']  
    return render(request,"checksheet.html",{'EMPID':EMPID,'WONO':WONO,'CATAGORY':CATAGORY,'HOURS':HOURS,'DESCRIPTION':DESCRIPTION})

def timesheet(request):
    return render(request,"timesheet.html")
    return HttpResponse(msg)

def workorder(request):
    msg="<h1>Manage you workorders here<h1>"
    return HttpResponse(msg)

def user(request):
    msg="<h1>Manage your account here<h1>"
    return HttpResponse(msg)

def contact(request):
    msg="<h1>Contact Admin for more Details<h1>"
    return HttpResponse(msg)
