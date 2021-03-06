from UserManager.models import Kargar, Customer
from .templatetags.toPersian import IntegerToPersian
from ReserveForm.date_manager.Miladi_To_Shamsi import convert_miladi_to_shamsi

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save, post_save

import datetime

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
    hasParche = models.BooleanField(verbose_name='پارچه دارد', default=False)
    parche = models.ForeignKey('Parche',verbose_name='پارچه', blank=True, null=True)
    parcheWidth = models.IntegerField(verbose_name='عرض پارچه', blank=True, null=True)
    parcheHeight = models.IntegerField(verbose_name='طول پارچه', blank=True, null=True)
    number = models.IntegerField(verbose_name='تعداد', blank=True, null=True)
    typeChap = models.ForeignKey('Chap', verbose_name='چاپ', blank=True, null=True)
    dookht = models.ForeignKey('Dookht', verbose_name='دوخت', blank=True, null=True,)
    hasLabel = models.BooleanField(verbose_name='لیبل دارد', default=False)
    otherServices = models.ManyToManyField('OtherServices', verbose_name='سایر خدمات', blank=True)
    # reserve date
    reserveDay = models.IntegerField(choices=dayChoice, verbose_name='روز', blank=True, null=True)
    reserveMonth = models.IntegerField(choices=monthChoice, verbose_name='ماه', blank=True, null=True)
    reserveYear = models.IntegerField(choices=yearChoice, verbose_name='سال', blank=True, null=True)
    # delivery date
    deliveryDay = models.IntegerField(choices=dayChoice, verbose_name='روز', blank=True, null=True)
    deliveryMonth = models.IntegerField(choices=monthChoice, verbose_name='ماه', blank=True, null=True)
    deliveryYear = models.IntegerField(choices=yearChoice, verbose_name='سال', blank=True, null=True)
    description = models.TextField(verbose_name='توضیح', blank=True, null=True)
    process = models.ForeignKey('Process', verbose_name='فرایند', blank=True, null=True, default=2)


    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش"

    def __str__(self):
        return str(self.id)

    def get_reserve_date(self):
        if self.reserveDay is not None and self.reserveMonth is not None and self.reserveYear is not None:
            return IntegerToPersian(self.reserveYear) + '/' + IntegerToPersian(self.reserveMonth) + '/' + IntegerToPersian(self.reserveDay)
        else:
            return '-'

    def get_delivery_date(self):
        if self.deliveryDay is not None and self.deliveryMonth is not None and self.deliveryYear is not None:
            return IntegerToPersian(self.deliveryYear) + '/' + IntegerToPersian(self.deliveryMonth) + '/' + IntegerToPersian(self.deliveryDay)
        else:
            return '-'

    def get_tarh_url(self):
        if self.tarh:
            return self.tarh.url
        else:
            return ''



class Parche(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت', blank=True, null=True)

    class Meta:
        verbose_name = 'پارچه'
        verbose_name_plural = 'پارچه'

    def __str__(self):
        return self.name



class Dookht(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت', blank=True, null=True)

    class Meta:
        verbose_name = 'دوخت'
        verbose_name_plural = 'دوخت'

    def __str__(self):
        return self.name



class ServiceTarh(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت',)

    class Meta:
        verbose_name = ' خدمات مربوط به طرح'
        verbose_name_plural = ' خدمات مربوط به طرح'

    def __str__(self):
        return self.name



class OtherServices(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    price = models.IntegerField(verbose_name='قیمت')

    class Meta:
        verbose_name = 'سایر خدمات'
        verbose_name_plural = 'سایر خدمات'

    def __str__(self):
        return self.name



class Chap(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)
    price = models.IntegerField(verbose_name='قیمت',)

    class Meta:
        verbose_name = 'چاپ'
        verbose_name_plural = 'چاپ'

    def __str__(self):
        return self.name



class Process(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام',)

    class Meta:
        verbose_name = 'فرایند'
        verbose_name_plural = 'فرایند'

    def __str__(self):
        return self.name



class ProcessFormKargar(models.Model):
    process = models.ForeignKey(Process, verbose_name='فرایند',)
    kargar = models.ForeignKey(Kargar, verbose_name='کارگر', null=True, blank=True)
    form = models.ForeignKey(ReserveForm, verbose_name='کد سفارش',)
    rate = models.IntegerField(verbose_name='امتیاز کارگر', null=True, blank=True, default=0)
    # start date
    startDay = models.IntegerField(choices=dayChoice, verbose_name='روز شروع', blank=True, null=True)
    startMonth = models.IntegerField(choices=monthChoice, verbose_name='ماه شروع', blank=True, null=True)
    startYear = models.IntegerField(choices=yearChoice, verbose_name='سال شروع', blank=True, null=True)
    # end date
    endDay = models.IntegerField(choices=dayChoice, verbose_name='روز اتمام', blank=True, null=True)
    endMonth = models.IntegerField(choices=monthChoice, verbose_name='ماه اتمام', blank=True, null=True)
    endYear = models.IntegerField(choices=yearChoice, verbose_name='سال اتمام', blank=True, null=True)
    # test widget
    startDateTime = models.DateTimeField(null=True, blank=True)
    endDateTime = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'وضعیت سفارش'
        verbose_name_plural = 'وضعیت سفارش'

    def get_duration(self):
        if self.startDateTime is None or self.endDateTime is None:
            return '-'
        duration = self.endDateTime - self.startDateTime
        hours, reminder = divmod(duration.seconds, 3600)
        return 'روز' + '\t' + str(duration.days) + ' | ' +     'ساعت' + str(hours)





def get_current_time():
    current_date_time = datetime.datetime.now()
    shamsi_date_time = convert_miladi_to_shamsi({'year':current_date_time.year, 'month':current_date_time.month, 'day':current_date_time.day})
    return IntegerToPersian(shamsi_date_time['year'])+'/'+IntegerToPersian(shamsi_date_time['month'])+'/'+IntegerToPersian(shamsi_date_time['day'])


#signals:

@receiver(post_save, sender=ReserveForm)
def reserveForm_post_save(sender, instance, created, **kwargs):
    if created == True:
        for process in Process.objects.all():
            processform = ProcessFormKargar()
            processform.process = process
            processform.form = instance
            processform.save()



@receiver(pre_delete, sender=ReserveForm)
def reserveForm_pre_delete(sender, instance, **kwargs):
    instance.tarh.delete(False)
    # form = ReserveForm.objects.get(id=1)
    # form.processformkargar_set
    # for process in instance.process_set.all():
    #     process.delete()
