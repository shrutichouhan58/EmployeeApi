from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=30)
    sal=models.IntegerField()
    address=models.CharField(max_length=60)
    mob=models.IntegerField()
    def __str__(self) -> str:
        return self.ename 