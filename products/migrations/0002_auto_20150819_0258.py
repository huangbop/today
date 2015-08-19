# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_hot',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_pep',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.FloatField(default=5),
        ),
    ]
