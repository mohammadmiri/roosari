# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReserveForm', '0017_remove_reserveform_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='processformkargar',
            name='endDateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='processformkargar',
            name='startDateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
