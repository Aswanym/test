from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Product(models.Model):


    CPU_COMPANY_CHOICE = (
        ('Intel','Intel'),
        ('AMD' , 'AMD')
    )
    RAM_CHOICE = (
        ('8','8'),
        ('16' , '16'),
        ('32' , '32'),
        ('64' , '64'),
        ('128' , '128'),
    )
    SECONDARY_MEMORY_CHOICE =(
        ('HDD','HDD'),
        ('SSD','SSD')
    )
    SECONDARY_STORAGE_CHOICE =(
        ('256 GB','256 GB'),
        ('512 GB','512 GB'),
        ('1 TB','1 TB'),
        ('2 TB','2 TB')
    )
    
    cpu_company = models.CharField(max_length=120, choices=CPU_COMPANY_CHOICE)
    ram = models.CharField(max_length=120,choices=RAM_CHOICE)
    secondary_memory = models.CharField(max_length=120,choices=SECONDARY_MEMORY_CHOICE)
    secondary_storage = models.CharField(max_length=120,choices=SECONDARY_STORAGE_CHOICE)
    external_cooling = models.BooleanField()

    case = models.CharField(max_length=120, blank=True, null=True)
    psu = models.CharField(max_length=120, blank=True, null=True)
    motherboard = models.CharField(max_length=120, blank=True, null=True)