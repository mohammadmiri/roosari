# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-15 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReserveForm', '0007_auto_20161030_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chap',
            options={'verbose_name_plural': 'چاپ'},
        ),
        migrations.AlterModelOptions(
            name='dookht',
            options={'verbose_name_plural': 'دوخت'},
        ),
        migrations.AlterModelOptions(
            name='parche',
            options={'verbose_name_plural': 'پارچه'},
        ),
        migrations.AlterModelOptions(
            name='process',
            options={'verbose_name_plural': 'فرایند'},
        ),
        migrations.AlterModelOptions(
            name='processformkargar',
            options={'verbose_name_plural': 'فرایند و سفارش'},
        ),
        migrations.AlterModelOptions(
            name='ReserveForm',
            options={'verbose_name_plural': 'سفارش'},
        ),
        migrations.AlterModelOptions(
            name='servicetarh',
            options={'verbose_name_plural': 'خدمات طرح'},
        ),
        migrations.AddField(
            model_name='ReserveForm',
            name='dookht',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ReserveForm.Dookht', verbose_name='دوخت'),
        ),
    ]
