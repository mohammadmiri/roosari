# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-07 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0013_auto_20161207_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='تیتر'),
        ),
    ]