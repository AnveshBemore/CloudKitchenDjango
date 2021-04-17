from django.shortcuts import render
from .models import udetails
from .models import product
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    nonvegmost=product.objects.filter(product_type="non_veg")
    vegmost=product.objects.filter(product_type="veg")
    
    msg={
        "nvdishes":nonvegmost,
        "vdishes":vegmost,
        "s":"signin",
    }
    return render(request,"index.html",msg)

def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")

def signupdb(request):
    if request.method=="POST":
        unam=request.POST["uname"]
        password=request.POST["password"]
        prod=udetails(uname=unam,password=password)
        prod.save()
        nonvegmost = product.objects.filter(product_type="non_veg")
        vegmost = product.objects.filter(product_type="veg")
        msg = {
            "nvdishes": nonvegmost,
            "vdishes": vegmost,
            "s": unam,
        }
    return render(request,"index.html",msg)

def verifylogin(request):
    if request.method=="POST":
        unam=request.POST["uname"]
        password=request.POST["password"]
        prod=udetails(uname=unam,password=password)
        prod.save()
        search=udetails.objects.filter(uname=unam)
        for i in search:
            print("-------------------"+i+"---------")
            if i.password==password:
                print(i.password)
                nonvegmost = product.objects.filter(product_type="non_veg")
                vegmost = product.objects.filter(product_type="veg")
                un=udetails.object.filter(uname=unam)
                msg = {
                    "nvdishes": nonvegmost,
                    "vdishes": vegmost,
                    "s":un,
                }
                print(un)
                return render(request,"index.html",msg)
        return render(request,"signup.html",{})
def menu(request):
    nonvegmost=product.objects.filter(product_type="non_veg")
    vegmost=product.objects.filter(product_type="veg")

    alldish=product.objects.all
    msg={
        "dishes":alldish,
        "nvdishes":nonvegmost,
        "vdishes":vegmost,
    }
    return render(request,"menu.html",msg)

def setorders(request):
    if request.method=="POST":
        nonvegmost=product.objects.filter(product_type="non_veg")
        vegmost=product.objects.filter(product_type="veg")

        alldish=product.objects.all
        msg={
            "dishes":alldish,
            "nvdishes":nonvegmost,
            "vdishes":vegmost,
        }
    # soup=BeautifulSoup(open("A:\\djangocloudkitchen\\cloudkitchen\\templates\\menu.html"),"html.parser")
    # for i in soup.find_all('span',{'class':'count'}):
    #     print("------------------------------------",i,"---------------------------------------")


    # print(soup) 

        print("ahiasdfagfaedg---------------hello------------------------------setorder------------------------")
        
        return render(request,"menu.html",msg)
    else:
        nonvegmost=product.objects.filter(product_type="non_veg")
        vegmost=product.objects.filter(product_type="veg")

        alldish=product.objects.all
        msg={
            "dishes":alldish,
            "nvdishes":nonvegmost,
            "vdishes":vegmost,
        }
        return render(request,"menu.html",msg)

def orders(request):
    return render(request,"orders.html")

def addorderindex(request):

    return index(request)