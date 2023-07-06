from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def Djangoform(request):
    SFO=Signupform()  ## it will collect data 
    d={'SFO':SFO}
    if request.method=='POST':
        SFDT=Signupform(request.POST) ## it will collect the data that received from the Frontend
        if SFDT.is_valid():    ## it will check the data whether the data is valid or not
            name=SFDT.cleaned_data['name']    ## this is the checking column of validaion 
            return HttpResponse(str(SFDT.cleaned_data))
    return render(request,'djangoform.html',d)
