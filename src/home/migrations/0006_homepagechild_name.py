# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagechild',
            name='name',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]