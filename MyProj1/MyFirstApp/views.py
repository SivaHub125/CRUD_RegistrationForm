from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas
# Create your views here.

def home(request):
    return render(request,'home.html')

"""def product(request):
    mobile=request.GET["mobile"]
    keyboard=request.GET["keyboard"]
    monitor=request.GET["monitor"]
    price=int(mobile)+int(keyboard)+int(monitor)
    return render(request,"result.html",{'Price':price})
"""
def register(request):
    name=request.POST['name']
    password=request.POST['password']
    address=request.POST['address']
    mail=request.POST['mail']
    return render(request,'output.html',{'Name':name,'Password':password,'Address':address,'Mail':mail})

def images(request):
    return render(request,'image.html')

def regmodel(request):
    mydata=Datas.objects.all()
    if(mydata!=''):
        return render(request,'register.html',{'datas':mydata})
    else:
        return render(request,'register.html')
    

def addData(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        contact=request.POST['contact']
        address=request.POST['address']
        mail=request.POST['mail']
        
        obj=Datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Mail=mail
        obj.save()
        mydata=Datas.objects.all()
        return redirect('regmodel')
    return render(request,'register.html')

def updateData(request,id):
    mydata=Datas.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        contact=request.POST['contact']
        address=request.POST['address']
        mail=request.POST['mail']

        mydata.Name=name
        mydata.Age=age
        mydata.Address=address
        mydata.Contact=contact
        mydata.Mail=mail
        mydata.save()
        return redirect('regmodel')
    return render(request,'update.html',{'data':mydata})

def deleteData(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect('regmodel')