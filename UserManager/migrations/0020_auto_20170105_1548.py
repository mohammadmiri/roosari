# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0019_auto_20161228_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='karbartehran',
            options={'verbose_name': 'فروشنده', 'verbose_name_plural': 'فروشنده'},
        ),
        migrations.AddField(
            model_name='karbarkarkhane',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='karbarKarkhane/', verbose_name='عکس'),
        ),
        migrations.AddField(
            model_name='karbartehran',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='karbarTehran/', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='karbartehran',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='karbartehran',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='karbartehran',
            name='password',
            field=models.CharField(max_length=100, verbose_name='رمز ورود'),
        ),
        migrations.AlterField(
            model_name='karbartehran',
            name='username',
            field=models.CharField(max_length=100, verbose_name='نام کاربری'),
        ),
    ]