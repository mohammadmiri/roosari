# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0003_auto_20161028_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
