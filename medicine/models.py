from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.

# add some attributes

class Drug(models.Model):
    drug_id = models.IntegerField(primary_key=True,default=0)
    drug_name = models.CharField(max_length=64,default='')
    add_time = models.DateTimeField(auto_now=True)
    drug_inventory = models.IntegerField(default=0)

    def __unicode__(self):
        return self.drug_name