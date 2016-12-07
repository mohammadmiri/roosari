# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-05 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0009_auto_20161124_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(verbose_name='روز')),
                ('month', models.IntegerField(verbose_name='ماه')),
                ('year', models.IntegerField(verbose_name='سال')),
                ('text', models.TextField(verbose_name='متن')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManager.Customer', verbose_name='مشتری')),
            ],
        ),
    ]