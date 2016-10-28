from django.db import models




class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام',)
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



