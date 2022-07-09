from django.contrib import admin
from django.urls import path
from auapp.views import usignup,ulogin,ulogout,uresetpassword
from eoapp.views import home,create,viewtask,deletetask

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("usignup/",usignup,name="usignup"),
    path("ulogin/",ulogin,name="ulogin"),
    path("ulogout/",ulogout,name="ulogout"),
    path("uresetpassword/",uresetpassword,name="uresetpassword"),
    path("create/",create,name="create"),
    path("viewtask/",viewtask,name="viewtask"),
    path("deletetask/<str:t>",deletetask,name="deletetask"),
]
