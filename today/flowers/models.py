from django.db import models


class Flower(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
