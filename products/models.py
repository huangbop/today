from django.db import models
from stdimage.models import StdImageField
from stdimage.utils import UploadToClassNameDir


class Product(models.Model):
    is_show = models.BooleanField(default=False)
    image = StdImageField(upload_to=UploadToClassNameDir(), blank=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    is_new = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)
    is_pep = models.BooleanField(default=False)
    rate = models.FloatField()
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
