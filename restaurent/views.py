from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *

def index(request):
    return render(request,"index.html")
def registerUser(request):
    return render(request,'registerUser.html')

def userReg(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        uemail=request.POST.get('uemail')
        uphone=request.POST.get('uphone')
        upassword=request.POST.get('upassword')
        insert=user_reg(uname=uname,uemail=uemail,uphone=uphone,upassword=upassword)
        insert.save()
        return render(request,'registerUser.html')
    
def loginPage(request):
    return render(request,'login.html') 

def loginFun(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username=="admin@gmail.com" and password=="admin":
            request.session['admin']='admin'
            return render(request,'index.html')
        elif user_reg.objects.filter(uemail=username,upassword=password).exists():
            cred=user_reg.objects.get(uemail=username,upassword=password)
            if cred.upassword==request.POST.get('password'):
                request.session['user']=cred.id
                return render(request,'index.html')
        else:
            return redirect(loginPage)
        
def logout(request):
    deletecart=cart.objects.all()
    deletecart.delete()
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(loginPage)

def addproduct(request):
    return render(request,'additem.html')

def additem(request):
    if request.method=='POST':
        pcode=request.POST.get('pcode')
        pname=request.POST.get('pname')
        pdescription=request.POST.get('pdescription')
        pqty=request.POST.get('pqty')
        pprice=request.POST.get('pprice')
        pfile=request.FILES['pfile']
        fs=FileSystemStorage()
        pimage=fs.save(pfile.name,pfile)
        insert=menu(pcode=pcode,pname=pname,pdescription=pdescription,pqty=pqty,pprice=pprice,pfile=pimage)
        insert.save()
        return redirect(addproduct)

def vmenu(request):
    items=menu.objects.all()
    return render(request,'menu.html',{'result':items})

sumqty=1
def addTocart(request,id):
    item=menu.objects.get(id=id)
    prcode=item.pcode
    prname=item.pname
    prprice=item.pprice
    prfile=item.pfile
    urid=request.session['user']
    sumqty=1
    if cart.objects.filter(prcode=prcode).exists():
        cartItem=cart.objects.get(prcode=prcode)
        cartid=cartItem.id
        itemqty=cartItem.prqty
        sumqty=int(sumqty)+int(itemqty)
        prtprice=int(sumqty)*int(prprice)
        update=cart(urid=urid,prcode=prcode,prname=prname,prprice=prprice,prqty=sumqty,prfile=prfile,prtprice=prtprice,id=cartid)
        update.save()
        return redirect(vmenu)
    else:
        prtprice=sumqty*prprice
        insert=cart(urid=urid,prcode=prcode,prname=prname,prprice=prprice,prqty=sumqty,prtprice=prtprice,prfile=prfile)
        insert.save()
        return redirect(vmenu)

def viewCart(request):
    cartItems=cart.objects.all()      
    total_price=sum(int(item.prprice)*int(item.prqty) for item in cartItems) 
    total_qty=sum(int(item.prqty) for item in cartItems)
    request.session['totalprice']=total_price
    
    return render(request,'viewcart.html',{'res':cartItems,'tprice':total_price,'tqty':total_qty})

def deleteFromcart(request,id):
    deleteItem=cart.objects.get(id=id)
    deleteItem.delete()
    return redirect(viewCart)

def viewUser(request):
    result=user_reg.objects.all()
    return render(request,'viewuser.html',{'users':result})

def viewitems(request):
    items=menu.objects.all()
    return render(request,'viewitems.html',{'items':items})
    
def deleteitem(request,id):
    delitem=menu.objects.get(id=id)
    delitem.delete()
    return redirect(viewitems)

def updateitempage(request,id):
    updateitem=menu.objects.get(id=id)
    return render(request,'updateitems.html',{'result':updateitem})

def updateitems(request,id):
    if request.method=='POST':
        ucode=request.POST.get('ucode')
        uname=request.POST.get('uname')
        udesc=request.POST.get('udescription')
        uqty=request.POST.get('uqty')
        uprice=request.POST.get('uprice')
        ufile=request.FILES['uimg']
        fss=FileSystemStorage()
        uimage=fss.save(ufile.name,ufile)
        update=menu(pcode=ucode,pname=uname,pdescription=udesc,pqty=uqty,pprice=uprice,pfile=uimage,id=id)
        update.save() 
        return redirect(viewitems)
    return redirect(viewitems)

def checkout(request):
    tprice=request.session['totalprice']
    if tprice<1:
        return redirect(vmenu)
    else:
        deletecart=cart.objects.all()
        deletecart.delete()
        return render(request,'checkout.html',{'res':tprice})
    



