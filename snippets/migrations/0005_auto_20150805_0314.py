# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.utils
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_snippet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='image',
            field=stdimage.models.StdImageField(null=True, upload_to=stdimage.utils.UploadToClassNameDir()),
        ),
    ]
