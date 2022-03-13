from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.forms import CharField
# Create your models here.

class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100 , null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=10 , null=True)
    district_id = models.IntegerField (null=True)
    school_id = models.IntegerField(null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class  Role(models.Model):
    admin = models.CharField(max_length=50, null=True)
    user = models.CharField(max_length=50 , null=True)
    

class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    # school_name = models.CharField(max_length=100, null=True)
    no_of_students = models.IntegerField()
    no_of_girls = models.IntegerField()
    no_of_boys = models.IntegerField()
    add_user = models.ForeignKey(User, on_delete=models.SET_NULL , null =True)
 

class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=200, null=True)
    no_of_schools = models.IntegerField()
    add_school = models.ForeignKey(School, on_delete=models.SET_NULL , null =True)
    add_user = models.ForeignKey(User, on_delete=models.SET_NULL , null =True)

 
   

  

   
