# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('moaref', models.CharField(max_length=200)),
                ('workPhoneNumber', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('companyName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Kargar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
