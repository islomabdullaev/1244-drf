from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=24)
    description = models.TextField()
    is_active = models.BooleanField(default=False)