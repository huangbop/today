from django.db import models
from stdimage.models import StdImageField
from stdimage.utils import UploadToClassNameDir


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='snippets', null=True)
    image = StdImageField(upload_to=UploadToClassNameDir(), null=True)

    class Meta:
        ordering = ('-created',)
