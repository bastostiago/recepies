from unicodedata import category
from django.db import models
from datetime import datetime

class Recepie(models.Model):
    recepie_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    prepare_mode = models.TextField()
    prepare_time = models.IntegerField()
    yields = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publish_datetime = models.DateTimeField(default=datetime.now, blank=True)
