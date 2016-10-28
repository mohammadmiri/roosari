from UserManager.models import Kargar, Customer

from django.db import models


class ReserveForm(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='مشتری',)
    tarh = models.ImageField(upload_to='tarh/', verbose_name='طرح',)
    serviceTarh = models.ManyToManyField('ServiceTarh', verbose_name='خدمات طرح',)
    hasParche = models.BooleanField(verbose_name='پارچه دارد',)
    parche = models.ForeignKey('Parche',verbose_name='پارچه',)
    parcheWidth = models.FloatField(verbose_name='عرض پارچه',)
    parcheHeight = models.FloatField(verbose_name='طول پارچه',)
    number = models.IntegerField(null=True, verbose_name='تعداد',)
    typeChap = models.ForeignKey('Chap', verbose_name='چاپ',)
    hasLabel = models.BooleanField(verbose_name='برچسب دارد',)
    dayChoice = (
        (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),
        (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31),
    )
    monthChoice = (
        (1, 'فروردین'),
        (2, 'اردیبهشت'),
        (3, 'خرداد'),
        (4, 'تیر'),
        (5, 'مرداد'),
        (6, 'شهریور'),
        (7, 'مهر'),
        (8, 'آبان'),
        (9, 'آذر'),
        (10, 'دی'),
        (11, 'بهمن'),
        (12, 'اسفند'),
    )
    # reserve date
    reserveDay = models.IntegerField(choices=dayChoice, verbose_name='روز',)
    reserveMonth = models.IntegerField(choices=monthChoice, verbose_name='ماه',)
    reserveYear = models.IntegerField(verbose_name='سال',)
    # delivery date
    deliveryDay = models.IntegerField(choices=dayChoice, verbose_name='روز',)
    deliveryMonth = models.IntegerField(choices=monthChoice, verbose_name='ماه',)
    deliveryYear = models.IntegerField(verbose_name='سال',)
    description = models.TextField(verbose_name='توضیح',)
    process = models.ForeignKey('Process', verbose_name='فرایند',)



class Parche(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت',)


class Dookht(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت',)


class ServiceTarh(models.Model):
    name = models.TextField(verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت',)


class Chap(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت',)


class Process(models.Model):
    name = models.TextField(verbose_name='نام',)


class ProcessFormKargar(models.Model):
    process = models.ForeignKey(Process, verbose_name='فرایند',)
    kargar = models.ForeignKey(Kargar, verbose_name='کارگر',)
    form = models.ForeignKey(ReserveForm, verbose_name='فرم',)






