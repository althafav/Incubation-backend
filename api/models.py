from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Application(models.Model):
    # STATUS = (
    #     ('New', 'New'),
    #     ('Pending', 'Pending'),
    #     ('Approved', 'Approved'),
    #     ('Declined', 'Declined'),
        
    # )
    
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=250 ,blank=True, null=True)
    city = models.CharField(max_length=100 ,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    companyname = models.CharField(max_length=150,blank=True, null=True)
    company_logo = models.ImageField(upload_to='companylogo/', null=True, blank=True)
   
    problem = models.TextField(max_length=500,blank=True, null=True)
    
    is_approved = models.BooleanField(default=False,blank=True, null=True)
    status = models.CharField(max_length=100,  default='Pending',blank=True, null=True)
    
    created_date    = models.DateTimeField(auto_now_add=True , null=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.companyname
    
    

# user register model

    
    
    
    
