from django.shortcuts import render
from Portfolio.models import Contact
from django.core.files.storage import FileSystemStorage
from .models import Skill, Project

# Create your views here.

def home(request) :
    return render(request,'home.html')
def about(request) :
    return render(request,'about.html')
def project(request) :
    return render(request,'project.html')
def contact(request):
    if request.method=='POST':
        obj=Contact()
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.concern=request.POST.get('concern')
        obj.save()
    return render(request,'contact.html')

def vieww(request):
    obj=Contact.objects.all()
    return render(request,'contact_view.html',{'x':obj})

def delete_std(request,pk):
    obj=Contact.objects.get(id=pk)
    obj.delete()
    return vieww(request)




 
 
 


