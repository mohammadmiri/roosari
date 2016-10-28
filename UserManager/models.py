from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, editable=False)
    name = models.CharField(max_length=100, null=True, verbose_name='نام')
    phoneNumber = models.CharField(max_length=50, verbose_name='شماره تلفن همراه',)
    email = models.EmailField(verbose_name='ایمیل',)
    moaref = models.CharField(max_length=200, verbose_name='نام معرف',)
    workPhoneNumber = models.CharField(max_length=50, verbose_name='تلفن محل کار',)
    address = models.TextField(verbose_name='آدرس',)
    companyName = models.TextField(verbose_name='نام شرکت',)

    def __str__(self):
        return self.name

class CustomerMessage(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='مشتری',)
    message = models.TextField(verbose_name='نامه',)

    def __str__(self):
        return self.message[:15]

class Kargar(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام',)

    def __str__(self):
        return self.name


@receiver(post_delete, sender=Customer)
def customer_post_delete(sender, instance, **kwargs):
    print('before delete in models'+str(type(instance))+' '+str(instance)+' '+str(instance.user))
    user = User.objects.get(id=instance.user.id)
    user.delete()




