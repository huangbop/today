# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150819_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_show',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.FloatField(),
        ),
    ]
