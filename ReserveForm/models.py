from UserManager.models import Kargar, Customer

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

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
yearChoice = ((1395, '۱۳۹۵'), (1396, '۱۳۹۶'), (1397, '۱۹۳۷'), (1398, '۱۳۹۸'), (1399, '۱۳۹۹'), (1400, '۱۴۰۰'), (1401, '۱۴۰۱'),
              (1402, '۱۴۰۲'), (1403, '۱۴۰۳'), (1404, '۱۴۰۴'), (1405, '۱۴۰۵'))


class ReserveForm(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='مشتری', )
    tarh = models.ImageField(upload_to='tarh/', verbose_name='طرح', blank=True, null=True)
    serviceTarh = models.ManyToManyField('ServiceTarh', verbose_name='خدمات طرح', blank=True)
    hasParche = models.BooleanField(verbose_name='پارچه دارد',)
    parche = models.ForeignKey('Parche',verbose_name='پارچه', blank=True, null=True)
    parcheWidth = models.FloatField(verbose_name='عرض پارچه', blank=True, null=True)
    parcheHeight = models.FloatField(verbose_name='طول پارچه', blank=True, null=True)
    number = models.IntegerField(verbose_name='تعداد', blank=True, null=True)
    typeChap = models.ForeignKey('Chap', verbose_name='چاپ', blank=True, null=True)
    dookht = models.ForeignKey('Dookht', verbose_name='دوخت', blank=True, null=True,)
    hasLabel = models.BooleanField(verbose_name='برچسب دارد', )

    # reserve date
    reserveDay = models.IntegerField(choices=dayChoice, verbose_name='روز', blank=True, null=True)
    reserveMonth = models.IntegerField(choices=monthChoice, verbose_name='ماه', blank=True, null=True)
    reserveYear = models.IntegerField(verbose_name='سال', blank=True, null=True)
    # delivery date
    deliveryDay = models.IntegerField(choices=dayChoice, verbose_name='روز', blank=True, null=True)
    deliveryMonth = models.IntegerField(choices=monthChoice, verbose_name='ماه', blank=True, null=True)
    deliveryYear = models.IntegerField(verbose_name='سال', blank=True, null=True)
    description = models.TextField(verbose_name='توضیح', blank=True, null=True)
    process = models.ForeignKey('Process', verbose_name='فرایند', blank=True, null=True)

    class Meta:
        verbose_name_plural = "1. سفارش ها"

    def __str__(self):
        return 'code: '+str(self.id)

class Parche(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت', blank=True, null=True)

    class Meta:
        verbose_name_plural = '2. پارچه'

    def __str__(self):
        return self.name



class Dookht(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت', blank=True, null=True)

    class Meta:
        verbose_name_plural = '3. دوخت'

    def __str__(self):
        return self.name



class ServiceTarh(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت',)

    class Meta:
        verbose_name_plural = '4. خدمات مربوط به طرح'

    def __str__(self):
        return self.name



class Chap(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت',)

    class Meta:
        verbose_name_plural = '5. چاپ'

    def __str__(self):
        return self.name



class Process(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)

    class Meta:
        verbose_name_plural = '6. فرایند'

    def __str__(self):
        return self.name



class ProcessFormKargar(models.Model):
    process = models.ForeignKey(Process, verbose_name='فرایند',)
    kargar = models.ForeignKey(Kargar, verbose_name='کارگر',)
    form = models.ForeignKey(ReserveForm, verbose_name='فرم',)
    # start date
    startDay = models.IntegerField(choices=dayChoice, verbose_name='روز شروع', blank=True, null=True)
    startMonth = models.IntegerField(choices=monthChoice, verbose_name='ماه شروع', blank=True, null=True)
    startYear = models.IntegerField(choices=yearChoice, verbose_name='سال شروع', blank=True, null=True)
    # end date
    endDay = models.IntegerField(choices=dayChoice, verbose_name='روز اتمام', blank=True, null=True)
    endMonth = models.IntegerField(choices=monthChoice, verbose_name='ماه اتمام', blank=True, null=True)
    endYear = models.IntegerField(choices=yearChoice, verbose_name='سال اتمام', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'وضعیت سفارش'






#signals:

@receiver(pre_delete, sender=ReserveForm)
def reserveForm_pre_delete(sender, instance, **kwargs):
    instance.tarh.delete(False)
