from django.db import models

class data_table(models.Model):
    items= models.CharField(max_length=255)
    is_labelled=models.BooleanField(default=False)
    label = models.CharField(max_length=255,null=True,blank=True)
