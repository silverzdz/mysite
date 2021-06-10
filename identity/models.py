from __future__ import unicode_literals
from django.db import models

# Create your models here.

class patient(models.Model):
    p_id = models.CharField(primary_key=True,max_length=64,default='')
    p_name = models.CharField(max_length=64,default='')
    p_telephone = models.CharField(max_length=64,default='')
    p_pw = models.CharField(max_length=40,default='')

    def __unicode__(self):
        return self.p_name

class doctor(models.Model):
    d_id = models.CharField(primary_key=True,max_length=64,default='')
    d_name = models.CharField(max_length=64,default='')
    d_telephone = models.CharField(max_length=64,default='')
    d_hospital = models.CharField(max_length=64,default='')
    d_department = models.CharField(max_length=64,default='')
    d_pw = models.CharField(max_length=40,default='')    

    def __unicode__(self):
        return self.d_name

class merchant(models.Model):
    m_id = models.CharField(primary_key=True,max_length=64,default='')
    m_name = models.CharField(max_length=64,default='')
    m_telephone = models.CharField(max_length=64,default='')
    m_pw = models.CharField(max_length=40,default='')

    def __unicode__(self):
        return self.m_name

class admin(models.Model):
    a_id = models.CharField(primary_key=True,max_length=64,default='')
    a_pw = models.CharField(max_length=40,default='')