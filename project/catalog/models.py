from django.db import models
from users.models import User

class Item(models.Model):
    title = models.CharField(max_length=200)
    path = models.ImageField(upload_to="img/%Y/%m/%d/", blank=True)
    description = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.user} on {self.item}'