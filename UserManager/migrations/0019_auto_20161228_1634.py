# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 16:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0018_remove_customer_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'مشتری', 'verbose_name_plural': 'مشتری'},
        ),
        migrations.AlterModelOptions(
            name='customermessage',
            options={'verbose_name': 'پیام مشتری', 'verbose_name_plural': 'پیام مشتری'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'رویداد', 'verbose_name_plural': 'رویداد'},
        ),
        migrations.AlterModelOptions(
            name='karbarkarkhane',
            options={'verbose_name': 'کاربر کارخانه', 'verbose_name_plural': 'کاربر کارخانه'},
        ),
        migrations.AlterModelOptions(
            name='karbartehran',
            options={'verbose_name': 'کاربر تهران', 'verbose_name_plural': 'کاربر تهران'},
        ),
        migrations.AlterModelOptions(
            name='kargar',
            options={'verbose_name': 'کارگر', 'verbose_name_plural': 'کارگر'},
        ),
    ]