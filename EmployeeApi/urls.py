
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.models import Employee
from home.EmpSerializer import Empserializer
from home.EmpViewset import Empviewset

router=routers.DefaultRouter()
router.register(r'Employees',Empviewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
