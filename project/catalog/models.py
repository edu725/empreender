from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    path = models.ImageField(upload_to="img/%Y/%m/%d/", blank=True)
    description = models.TextField()