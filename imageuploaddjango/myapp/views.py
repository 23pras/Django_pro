import os
from django.shortcuts import render,redirect  
from django.http import HttpResponse  
from myapp.functions import imageupload
from myapp.forms import *  
def show(request):  
    if request.method == 'POST':  
        img = ImageForm(request.POST, request.FILES)  
        if img.is_valid(): 
            img.save()
            imageupload(request.FILES['file']) 
            return HttpResponse("File uploaded successfuly")  
    else:  
        img =ImageForm()  
    return render(request,"index.html",{'form':img})  
