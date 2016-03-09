from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    shirt_size_choices = (('s', 'small'),
                          ('m', 'medium'),
    )
    shirt_size = models.CharField(max_length=1, choices=shirt_size_choices,
                                  default='s')
