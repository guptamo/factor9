# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 20:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='post_date',
        ),
    ]