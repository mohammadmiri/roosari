# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 12:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0025_auto_20170114_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karbarkarkhane',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
