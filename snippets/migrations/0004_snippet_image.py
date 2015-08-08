# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_snippet_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='image',
            field=stdimage.models.StdImageField(upload_to='~', null=True),
        ),
    ]
