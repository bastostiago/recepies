from unicodedata import category
from django.db import models
from datetime import datetime
from people.models import People

class Recepie(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    recepie_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    prepare_mode = models.TextField()
    prepare_time = models.IntegerField()
    yields = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publish_datetime = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self) -> str:
        return self.recepie_name
