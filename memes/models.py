from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Meme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    joke = models.TextField(max_length=1000)
    description = models.TextField(null=True, blank=True)
