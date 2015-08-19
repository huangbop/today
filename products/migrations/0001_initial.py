# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.utils
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('is_show', models.BooleanField()),
                ('image', stdimage.models.StdImageField(upload_to=stdimage.utils.UploadToClassNameDir(), blank=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('description', models.CharField(max_length=500, blank=True)),
                ('is_new', models.BooleanField()),
                ('is_hot', models.BooleanField()),
                ('is_pep', models.BooleanField()),
                ('rate', models.FloatField()),
                ('price', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
