from django.shortcuts import render,redirect
from .models import udetails
from .models import orders
from .models import product
from .models import ordershistory
from bs4 import BeautifulSoup
# Create your views here.
# from .config import username
from . import config
# username="ck"
un="hello"
def index(request):
    nonvegmost=product.objects.filter(product_type="non_veg")
    vegmost=product.objects.filter(product_type="veg")
    countorders=orders.objects.values("numofprod")
    coun=0
    for i in countorders:
        coun+=int(i.get("numofprod"))
        print("count cccccccc "+str(i.get("numofprod")))
        
    print("ppppppppppppppp "+str(coun))
    msg={
        "nvdishes":nonvegmost,
        "vdishes":vegmost,
        "uname":"signin",
        "countorders":coun,
    }
    return render(request,"index.html",msg)
    # return redirect("login/") 

def login(request):
    user={
        "alreadyuser":""
    }
    return render(request,"login.html",user)
    
def signup(request):
    return render(request,"signup.html")

def verifylogin(request):
    if request.method=="POST":
        unam=request.POST["uname"]
        password=request.POST["password"]
        prod=udetails(uname=unam,password=password)
        search=udetails.objects.filter(uname=unam)
        for i in search:
            print("-------------------"+str(i)+"---------")
            if i.password==password:
                print(i.password)
                nonvegmost = product.objects.filter(product_type="non_veg")
                vegmost = product.objects.filter(product_type="veg")
                global un
                # un=udetails.objects.filter(uname=unam)

                un=unam
                print("hellllllllllooooooooooo thiiiiiiis     iiiiiiiiiiissssss "+un)
                config.username=un
                print("usssssssssserrrrnnnnnnnaaaaaaaaamee "+str(config.username))
                print(str(un)+"]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                msg = {
                    "nvdishes": nonvegmost,
                    "vdishes": vegmost,
                    "uname":un,
                }
                return render(request,"index.html",msg)
        return render(request,"signup.html",{})
    return redirect("index")


def signupdb(request):
    if request.method=="POST":
        unam=request.POST["uname"]
        password=request.POST["password"]
        search=udetails.objects.filter(uname=unam)
        print(search)
        if not search:
            
            prod=udetails(uname=unam,password=password)
            print("signup login------------------- uname"+unam+"  pasw "+password)
            prod.save()
        else:            
            user={
                "alreadyuser":"already user please login"
            }
            return render(request,"login.html",user)
        nonvegmost=product.objects.filter(product_type="non_veg")
        vegmost=product.objects.filter(product_type="veg")
        
        msg={
            "nvdishes":nonvegmost,
            "vdishes":vegmost,
            "uname":unam,
        }
        return render(request,"index.html",msg)

    return render(request,"index.html",msg)
    # return redirect("")

def menu(request):
    nonvegmost=product.objects.filter(product_type="non_veg")
    vegmost=product.objects.filter(product_type="veg")
    print("usssssssssserrrrnnnnnnnaaaaaaaaamee "+str(config.username))

    alldish=product.objects.all
    msg={
        "dishes":alldish,
        "nvdishes":nonvegmost,
        "vdishes":vegmost,
        "uname":"signin",
    }
    return render(request,"menu.html",msg)

def setorders(request):
    if request.method=="GET":
        id=request.GET.get("id")
        ty=request.GET.get("type")
        print("mmmmmmmmmmmmmmmmmmm--------from which html----------- "+str(ty))
        print("entered ddddddd set orders  function  1111111111111111111111111")
        print("iiiiiiiiiiiiiiiiiiiiiii add order "+id)
        prodDetails=product.objects.filter(product_id=id)
        ordered_item=orders.objects.filter(order_id_id=id)
        for i in ordered_item:
            print("enterred i order_temes 22222222222")
            no_of_orders_item=i.numofprod
            (no_of_orders_item)+=1
            print(no_of_orders_item)
            orders_add_update=orders.objects.get(order_id_id=id)
            orders_add_update.numofprod=no_of_orders_item
            print("nooforders --------- "+str(orders_add_update.order_id_id))

            orders_add_update.save()
            if ty=="index":
                return redirect("index")
            else:
                return redirect("menu")
       
        for i in prodDetails:
            print(i.product_name+" kkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            
            ord=orders(order_id_id=i.product_id,order_name=i.product_name,order_price=i.product_price,order_img=i.product_img,name=config.username)
            
            ord1=ordershistory(order_id_id=i.product_id,order_name=i.product_name,order_price=i.product_price,order_img=i.product_img,name=config.username)
            print("3333333333333 enter to save")
            ord.save()

        if ty=="index":
            return redirect("index")
        else:
            return redirect("menu")
    # if request.method=="GET":
    #     nonvegmost=product.objects.filter(product_type="non_veg")
    #     vegmost=product.objects.filter(product_type="veg")

    #     alldish=product.objects.all
    #     msg={
    #         "dishes":alldish,
    #         "nvdishes":nonvegmost,
    #         "vdishes":vegmost,
    #     }
    # soup=BeautifulSoup(open("A:\\djangocloudkitchen\\cloudkitchen\\templates\\menu.html"),"html.parser")
    # for i in soup.find_all('span',{'class':'count'}):
    #     print("------------------------------------",i,"---------------------------------------")


    # print(soup) 

    #     print("ahiasdfagfaedg---------------hello------------------------------setorder------------------------")
        
    #     return render(request,"menu.html",msg)
    # else:
    #     nonvegmost=product.objects.filter(product_type="non_veg")
    #     vegmost=product.objects.filter(product_type="veg")

    #     alldish=product.objects.all
    #     msg={
    #         "dishes":alldish,
    #         "nvdishes":nonvegmost,
    #         "vdishes":vegmost,
    #     }
    #     return render(request,"menu.html",msg)
def minusorders(request):
    if request.method=="GET":
        id=request.GET.get("id")
        ty=request.GET.get("type")
        print("mmmmmmmmmmmmmmmmmmm--------from which html----------- "+str(ty))
        print("iiiiiiiiiiiiiiiiiiiiiii   del "+str(id))
        prodDetails=product.objects.filter(product_id=id)
        ordered_item=orders.objects.filter(order_id_id=id)
        for i in ordered_item:
            no_of_orders_item=i.numofprod
            if no_of_orders_item==1:
                orders.objects.filter(order_id_id=id).delete()
                if ty=="index":
                    return redirect("index")
                else:
                    return redirect("menu")

            (no_of_orders_item)-=1
            print(no_of_orders_item)
            order_del_save=orders.objects.get(order_id_id=id)
            order_del_save.numofprod=no_of_orders_item
            order_del_save.save()
            
            if ty=="index":
                return redirect("index")
            else:
                return redirect("menu")
        # for i in prodDetails:
        #     print(i.product_name+"kkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        #     j=i.product_name
        #     ord=orders(order_id_id=i.product_id,order_name=j,order_price=i.product_price,order_img=i.product_img)
        #     ord.save()

        return redirect("index")
def displayorders(request):
     disorders=orders.objects.all
     msg={
         "ordereditems":disorders,
     }
     print("hellllllllllooooooooooo thiiiiiiis    iiiiiiiiiiissssss "+un)
     return render(request,"displayorders.html",msg)






# def addorderindex(request):

#     return index(request)
# def doorder(request):
#     id=request.GET.get('id')
#     print(id)
#     return render(request,"menu.html")
# def localstorage(request):
#     sum={"s":0}
#     return render(request,"localstorage.html",sum)

# def add(request):
#     # n=request.form
#     num1=int(request.GET.get("num1"))

#     num2=int(request.GET.get("num2"))
#     add=num1+num2
#     sum={"s":add}
#     print(str(add)+"-----------")

#     return render(request,"localstorage.html",sum)

# def plus(request):
    
#     return redirect("index")

def displaybill(request):
    if request.method=="POST":
        # E
        name=request.POST["name"]
        address=request.POST["address"]
        phnnum=request.POST["phnnum"]
        paymentDetails="details"
        if request.POST["credit"]!="":
            paymentDetails=request.POST["credit"]
        if request.POST["debit"]!="":
            paymentDetails=request.POST["debit"]
        if request.POST["upi"]!="":
            paymentDetails=request.POST["upi"]
        if request.POST["netbanking"]!="":
            paymentDetails=request.POST["netbanking"]
        print("cccccashondel  ------------"+str(request.POST.get("cashondelivary",False)))
        if request.POST.get("cashondelivary",False)!=False:
            paymentDetails="cash on delivary"
        # debit=request.POST["credit"]
        # upi=request.POST["upi"]
        # netbanking=request.POST["netbanking"]
        # cashondel=request.POST["cashondelivary"]
        ordall=orders.objects.all()

        for o in ordall:
            # print("helllllllllo   id "+str(o.order_id)+" ordername "+o.order_name)
            print("ooooooo "+str(o.numofprod))
            ordhis=ordershistory(order_id_id=o.order_id_id,order_name=o.order_name,order_price=o.order_price,order_img=o.order_img,numofprod=o.numofprod,name=name)
            ordhis.save()
            orders.objects.all().delete()
        msg={
            "name":name,
            "address":address,
            "phnnum":phnnum,
            "payment":paymentDetails,
            
        }
        # or=orders(order_id=)
        
        return render(request,"displaybill.html",msg)
    return redirect("displayorders")

def posi(request):
    return render(request,"position.html")