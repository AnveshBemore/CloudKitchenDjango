from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns=[
     path("",views.index,name="index"),
     path("index",views.index,name="index"),
     path("login/",views.login,name="login"),
     path("login/signup/index",views.index,name="index"), 
     path("login/signup/",views.signup,name="signup"),
     path("login/signup/signupdb",views.signupdb,name="signupdb"),
     path("login/signup/verifylogin",views.verifylogin,),
     path("login/verifylogin",views.verifylogin,name="verifylogin"),
     path("login/menu",views.menu,name="menu"),
     path("menu",views.menu,name="menu"),
     path("setorders/",views.setorders,name="setorders"), 
     path("login/setorders/",views.setorders,name="setorders"),
     path("login/signup/setorders/",views.setorders,name="setorders"),
     path("deleteorders/",views.minusorders,name="minusorders"),
     path("login/deleteorders/",views.minusorders,name="minusorders"),
     path("login/signup/deleteorders/",views.minusorders,name="minusorders"),
     path("displayorders",views.displayorders,name="displayorders"),
     # path("addorderindex",views.addorderindex,name="addorderindex"),
     path("login/signupdb",views.signupdb,name="signupdb"),
     # path("addorder",views.doorder,name="doorders"),
     # path("add",views.add,name="add")
     
     path("displaybill/",views.displaybill,name="displaybill"),
]