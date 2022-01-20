from django.db import models

class SampleFormData(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname=models.CharField(max_length=30)
    gender=models.CharField(max_length=6)
    email=models.EmailField()
    phone_number=models.CharField(max_length=11)