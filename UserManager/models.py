from django.db import models




class Customer(models.Model):
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=50)
    email = models.EmailField()
    moaref = models.CharField(max_length=200)
    workPhoneNumber = models.CharField(max_length=50)
    address = models.TextField()
    companyName = models.TextField()


class CustomerMessage(models.Model):
    customer = models.ForeignKey(Customer)
    message = models.TextField()


class Kargar(models.Model):
    name = models.CharField(max_length=200)




