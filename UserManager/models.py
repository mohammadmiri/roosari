from django.db import models
from ReserveForm.date_manager.Miladi_To_Shamsi import convert_miladi_to_shamsi
from ReserveForm.templatetags.toPersian import IntegerToPersian

from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver

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


class Customer(models.Model):
    user = models.OneToOneField(User, )
    username = models.CharField(max_length=100, verbose_name='نام کاربری')
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='نام')
    phoneNumber = models.CharField(max_length=50, verbose_name='شماره تلفن همراه', blank=True, null=True)
    email = models.EmailField(verbose_name='ایمیل',)
    moaref = models.CharField(max_length=200, verbose_name='نام معرف', blank=True, null=True)
    workPhoneNumber = models.CharField(max_length=50, verbose_name='تلفن محل کار', blank=True, null=True)
    address = models.TextField(verbose_name='آدرس', null=True, blank=True)
    companyName = models.CharField(verbose_name='نام شرکت', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری'

    def __str__(self):
        return str(self.id)+' '+self.name



class CustomerMessage(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='مشتری',)
    date = models.DateTimeField(verbose_name='تاریخ', null=True, blank=True)
    message = models.TextField(verbose_name='نامه',)
    is_read = models.BooleanField(verbose_name='خوانده شده', blank=True, default=False)


    class Meta:
        verbose_name = 'پیام مشتری'
        verbose_name_plural = 'پیام مشتری'

    def __str__(self):
        return self.message[:15]

    def get_date(self):
        if self.date is not None:
            shamsi_date_time = convert_miladi_to_shamsi({'year': self.date.year, 'month': self.date.month, 'day': self.date.day})
            return IntegerToPersian(shamsi_date_time['year']) + '/' + IntegerToPersian(
                shamsi_date_time['month']) + '/' + IntegerToPersian(shamsi_date_time['day'])
        else:
            return '-'

    def get_time(self):
        if self.date is not None:
            time = self.date + datetime.timedelta(0, 12600)
            return str(time.hour) + ':' + str(time.minute)
        else:
            return '-'


class Kargar(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام',)

    class Meta:
        verbose_name = 'کارگر'
        verbose_name_plural = 'کارگر'

    def __str__(self):
        return self.name


class AdminSite(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=100, verbose_name='نام کاربری', )
    password = models.CharField(max_length=100, verbose_name='رمز ورود', )
    name = models.CharField(max_length=100, verbose_name='نام', )
    email = models.EmailField(null=True, verbose_name='ایمیل', )
    image = models.ImageField(upload_to='karbarTehran/', verbose_name='عکس', null=True, blank=True)

    class Meta:
        verbose_name = 'ادمین'
        verbose_name_plural = 'ادمین'

    def __str__(self):
        return self.username

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return '/static/img/anonymous.png'


class KarbarTehran(models.Model):
    user = models.OneToOneField(User, )
    username = models.CharField(max_length=100, verbose_name='نام کاربری',)
    password = models.CharField(max_length=100, verbose_name='رمز ورود',)
    name = models.CharField(max_length=100, verbose_name='نام',)
    email = models.EmailField(null=True, verbose_name='ایمیل',)
    image = models.ImageField(upload_to='karbarTehran/', verbose_name='عکس', null=True, blank=True)

    class Meta:
        verbose_name = 'فروشنده'
        verbose_name_plural = 'فروشنده'

    def __str__(self):
        return self.username

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return '/static/img/anonymous.png'


class KarbarKarkhane(models.Model):
    user = models.OneToOneField(User,)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to='karbarKarkhane/', verbose_name='عکس', null=True, blank=True)

    class Meta:
        verbose_name = 'کاربر کارخانه'
        verbose_name_plural = 'کاربر کارخانه'

    def __str__(self):
        return self.username

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return '/static/img/anonymous.png'


class Event(models.Model):
    day = models.IntegerField(verbose_name='روز', choices=dayChoice)
    month = models.IntegerField(verbose_name='ماه', choices=monthChoice)
    year = models.IntegerField(verbose_name='سال', choices=yearChoice)
    customer = models.ForeignKey(Customer, verbose_name='مشتری', )
    title = models.CharField(verbose_name='تیتر', max_length=200, null=True, blank=True)
    text = models.TextField(verbose_name='متن', )

    class Meta:
        verbose_name = 'رویداد'
        verbose_name_plural = 'رویداد'

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return 'static/img/anonymous.png'

#signals:

@receiver(post_delete, sender=Customer)
def customer_post_delete(sender, instance, **kwargs):
    user = User.objects.get(id=instance.user.id)
    user.delete()


@receiver(post_delete, sender=KarbarTehran)
def karbarTehran_post_delete(sender, instance, **kwargs):
    user = User.objects.get(id=instance.user.id)
    user.delete()


@receiver(post_delete, sender=KarbarKarkhane)
def karbarKarkhane_post_delete(sender, instance, **kwargs):
    user = User.objects.get(id=instance.user.id)
    user.delete()