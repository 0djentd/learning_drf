from django.db import models

# Create your models here.
class Meme(models.Model):
    name = models.CharField(max_length=100)
    joke = models.TextField(max_length=1000)
    description = models.TextField(null=True, blank=True)
