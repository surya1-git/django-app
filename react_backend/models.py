from django.db import models

# Create your models here.

class CsvData(models.Model):

    image_name = models.CharField(max_length=200,null=True,blank=True)
    objects_detected = models.CharField(max_length=200,null=True,blank=True)
    timestamp = models.DateField(max_length=50,null=True,blank=True)