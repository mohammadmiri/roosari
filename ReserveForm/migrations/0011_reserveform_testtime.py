# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-03 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReserveForm', '0010_auto_20161126_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserveform',
            name='testtime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ برای تست widget'),
        ),
    ]