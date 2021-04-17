from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns=[
     path("",views.index,name="index"),
     path("login/",views.login,name="login"),
     path("login/signup/index",views.index,name="index"),
     path("login/signup/",views.signup,name="signup"),
     path("login/signup/signupdb",views.signupdb,name="signupdb"),
     path("login/verifylogin",views.verifylogin,name="verifylogin"),
     path("login/menu",views.menu,name="menu"),
     path("setorders",views.setorders,name="setorders"),
     path("orders",views.orders,name="orders"),
     path("addorderindex",views.addorderindex,name="addorderindex"),
     path("login/signupdb/",views.signupdb,name="signupdb"),
     
]