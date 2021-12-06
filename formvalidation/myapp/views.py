from django.shortcuts import render
from myapp.forms import *
# Create your views here.
def show(request):
    if request.method=='POST':
        eform=LoginForm(request.POST)
        if eform.is_valid():
            eform.save()
            return render(request,'index.html')
    else:
        eform=LoginForm()
    return render(request,'index.html',{'form':eform})