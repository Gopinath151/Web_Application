from django.db import models
from django.utils.timezone import now

# Create your models here.

class Registration(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=220,null=True)
    Points = models.IntegerField(null=True)
    path = models.CharField(max_length=230,null=True)
    flag = models.IntegerField(null=True)
    status = models.IntegerField(default=1)
    created_by = models.CharField(max_length=200)
    created_date = models.DateField(default=now)
    updated_by = models.CharField(max_length=200,null=True)
    updated_date = models.DateTimeField(null=True)


class Admin_Login(models.Model):
    App_name = models.CharField(max_length=220)
    App_URL = models.CharField(max_length=220)
    App_category = models.CharField(max_length=220,null=True)
    Subcategory= models.CharField(max_length=220,null=True)
    points = models.IntegerField(null=True)
    Path= models.CharField(max_length=255, null=True)
    # images=models.FileField(upload_to='Imagepath/',null=True)

