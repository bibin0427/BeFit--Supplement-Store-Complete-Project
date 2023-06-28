from django.db import models


# Create your models here.
class Customerdb(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirmpassword = models.CharField(max_length=100, null=True, blank=True)

class checkoutdetailsdb(models.Model):
    Firstname=models.CharField(max_length=100,null=True,blank=True)
    Lastname=models.CharField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    City=models.CharField(max_length=100,null=True,blank=True)
    Postcode=models.IntegerField(null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)