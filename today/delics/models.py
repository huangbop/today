from django.db import models

from today.users.models import User


class Delic(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10)

    def __str__(self):
        return self.title
