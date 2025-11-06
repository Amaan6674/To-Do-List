from django.contrib import admin
from django.urls import path
from auapp.views import usignup,ulogin,ulogout,uresetpassword,guest_login
from eoapp.views import home,create,viewtask,deletetask,completetask

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("usignup/",usignup,name="usignup"),
    path("ulogin/",ulogin,name="ulogin"),
    path("ulogout/",ulogout,name="ulogout"),
    path("guest-login/",guest_login,name="guest_login"),
    path("uresetpassword/",uresetpassword,name="uresetpassword"),
    path("create/",create,name="create"),
    path("viewtask/",viewtask,name="viewtask"),
    path("deletetask/<str:t>",deletetask,name="deletetask"),
    path("completetask/<str:t>",completetask,name="completetask"),
]
