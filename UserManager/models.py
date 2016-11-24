from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver

class Customer(models.Model):
    user = models.OneToOneField(User, editable=False)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True, verbose_name='نام')
    phoneNumber = models.CharField(max_length=50, verbose_name='شماره تلفن همراه',)
    email = models.EmailField(verbose_name='ایمیل',)
    moaref = models.CharField(max_length=200, verbose_name='نام معرف',)
    workPhoneNumber = models.CharField(max_length=50, verbose_name='تلفن محل کار',)
    address = models.TextField(verbose_name='آدرس',)
    companyName = models.TextField(verbose_name='نام شرکت',)

    class Meta:
        verbose_name_plural = 'مشتری'

    def __str__(self):
        return self.name


class CustomerMessage(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='مشتری',)
    message = models.TextField(verbose_name='نامه',)

    class Meta:
        verbose_name_plural = 'پیام مشتری'

    def __str__(self):
        return self.message[:15]


class Kargar(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام',)

    class Meta:
        verbose_name_plural = 'کارگر'

    def __str__(self):
        return self.name



class KarbarTehran(models.Model):
    user = models.OneToOneField(User, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)

    class Meta:
        verbose_name_plural = 'کاربر تهران'

    def __str__(self):
        return self.username


class KarbarKarkhane(models.Model):
    user = models.OneToOneField(User, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)

    class Meta:
        verbose_name_plural = 'کاربر کارخانه'

    def __str__(self):
        return self.username



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