from rest_framework import serializers
from home.models import Employee
from home.EmpSerializer import Empserializer
from rest_framework import viewsets

class Empviewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializer