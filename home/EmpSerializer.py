from rest_framework import serializers
from home.models import Employee
class Empserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"