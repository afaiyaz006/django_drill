from django.db import models

# Creating my models here.
class Student(models.Model):
    reg_id=models.CharField(primary_key=True,max_length=8)
    name=models.CharField(max_length=20)
    batch_no=models.IntegerField()
