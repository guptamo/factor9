# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
