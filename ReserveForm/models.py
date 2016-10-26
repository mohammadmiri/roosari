from UserManager.models import Kargar, Customer

from django.db import models


class ReserveForm(models.Model):
    customer = models.ForeignKey(Customer)
    tarh = models.ImageField(upload_to='tarh/')
    serviceTarh = models.ManyToManyField('ServiceTarh')
    hasParche = models.BooleanField()
    parche = models.ForeignKey('Parche')
    parcheWidth = models.FloatField()
    parcheHeight = models.FloatField()
    number = models.IntegerField(null=True, )
    typeChap = models.ForeignKey('Chap')
    hasLabel = models.BooleanField()
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
    reserveDay = models.IntegerField(choices=dayChoice)
    reserveMonth = models.IntegerField(choices=monthChoice)
    reserveYear = models.IntegerField()
    # delivery date
    deliveryDay = models.IntegerField(choices=dayChoice)
    deliveryMonth = models.IntegerField(choices=monthChoice)
    deliveryYear = models.IntegerField()
    description = models.TextField()
    process = models.ForeignKey('Process')



class Parche(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


class Dookht(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


class ServiceTarh(models.Model):
    name = models.TextField()
    price = models.IntegerField()


class Chap(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


class Process(models.Model):
    name = models.TextField()


class ProcessFormKargar(models.Model):
    process = models.ForeignKey(Process)
    kargar = models.ForeignKey(Kargar)
    form = models.ForeignKey(ReserveForm)






