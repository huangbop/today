from django.db import models
from stdimage.models import StdImageField
from stdimage.utils import UploadToClassNameDir


class Product(models.Model):
    is_show = models.BooleanField(default=True)
    image = StdImageField(upload_to=UploadToClassNameDir(), blank=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    is_new = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)
    is_pep = models.BooleanField(default=False)
    rate = models.FloatField(default=5)
    price = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
