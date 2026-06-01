from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import contact_table
# Create your views here.
def welcome (request):
    return HttpResponse("hello welcome Django")


def addcontact(request): 
    return render(request,'add contact.html')


def viewcontact(request):
    data=contact_table.objects.all()
    return render(request,'view contact.html',{"data":data})



def add_contact_post(request):
    name=request.POST["name"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    print(name,email,phone)
    ob=contact_table()
    ob.name = name 
    ob.email = email
    ob.phone = phone
    ob.save()
    return HttpResponse("ok")

def deletecontact(requst,id):
    contact_table.objects.filter(id=id).delete()
    return HttpResponse("deleted")
 
def editcontact(request):
    request.session['eid']= id
    data=contact_table,object.get (id=id)
    return render(request,'edit contact.html',{"data":data})


def edit_contact_post(request):
    name=request.POST["name"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    print(name,email,phone)

    id=request.session['eid']
    ob=contact_table.objects.get(id=id)
    ob.name = name 
    ob.email = email
    ob.phone = phone
    ob.save()
    return HttpResponse("ok")
                  




