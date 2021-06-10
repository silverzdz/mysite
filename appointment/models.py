from __future__ import unicode_literals
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import deactivate
from identity.models import patient, doctor
import datetime

# Create your models here.

class register(models.Model):
    r_id = models.IntegerField(primary_key=True,default=0)
    r_hospital = models.CharField(max_length=64,default='')
    r_department = models.CharField(max_length=64,default='')
    r_time = models.DateField(default=datetime.date(1970,1,1))
    p_id = models.ForeignKey(patient,on_delete=models.CASCADE,default='')
    d_id = models.ForeignKey(doctor,on_delete=models.CASCADE,default='')

class covid(models.Model):
    c_id = models.IntegerField(primary_key=True,default=0)
    # 1 for testing, 2 for vaccine
    c_type = models.IntegerField(default=0)
    c_hospital = models.CharField(max_length=64,default='')
    c_time = models.DateField(default=datetime.date(1970,1,1))
    p_id = models.ForeignKey(patient,on_delete=models.CASCADE,default='')

