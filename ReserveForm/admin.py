from .models import Dookht, Chap, Process, Parche, ReserveForm, ProcessFormKargar, ServiceTarh
from UserManager.models import CustomerMessage

from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.shortcuts import reverse
from django.conf.urls import url


class ProcessInline(admin.TabularInline):
    model = ProcessFormKargar
    extra = 1
    fieldsets = (
        ('فرایند', {
            'fields':('process',)
        }),
        ('کارگر', {
            'fields':('kargar',)
        }),
        ('زمان شروع', {
            'fields':('startDay', 'startMonth', 'startYear',)
        }),
        ('زمان اتمام', {
            'fields':('endDay', 'endMonth', 'endYear',)
        }),
    )

class ReserveFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_customer_name',)
    list_display_links = ('get_customer_name',)
    search_fields = ['id']

    def get_customer_name(self, obj):
        return obj.customer.name


    fieldsets = (
        ('مشتری', {
            'fields':('customer', )
        }),
        ('طرح', {
            'fields':('tarh', 'serviceTarh',)
        }),
        ('پارچه', {
            'fields':('hasParche', 'parche', )
        }),
        ('اندازه', {
            'fields':('parcheWidth', 'parcheHeight', )
        }),
        ('دوخت', {
            'fields':('dookht', 'hasLabel')
        }),
        ('اطلاعات', {
            'fields':('typeChap', 'number')
        }),
        ('زمان سفارش',{
            'fields':('reserveDay', 'reserveMonth', 'reserveYear',),
        }),
        ('زمان تحویل', {
            'fields':('deliveryDay', 'deliveryMonth', 'deliveryYear', )
        }),
        ('اطلاعات', {
            'fields':('description', 'process', )
        }),
    )

    formfield_overrides = {
        models.ManyToManyField: {'widget':CheckboxSelectMultiple},
    }

    def get_readonly_fields(self, request, obj=None):
        groupnames = request.user.groups.values_list('name', flat=True)
        print('group name:'+str(groupnames))
        if 'admin' in groupnames:
            return ()
        elif 'karbarTehran' in groupnames:
            return ()
        elif 'karbarKarkhane' in groupnames:
            print('in group')
            return ('customer', 'tarh', 'serviceTarh', 'hasParche', 'parche', 'parcheWidth', 'parcheHeight', 'typeChap', 'hasLabel',
                    'reserveDay', 'reserveMonth', 'reserveYear', 'deliveryDay', 'deliveryMonth', 'deliveryYear', 'description',
                     'dookht',)
        else:
            return ()

    def save_model(self, request, obj, form, change):
        if change and 'tarh' in form.changed_data:
            reserve = ReserveForm.objects.get(id=obj.id)
            reserve.tarh.delete(False)
        obj.save()



class DookhtAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'price',)
    list_display_links = ('name',)


class ParcheAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'price',)
    list_display_links = ('name',)


class ChapAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_display_links = ('name',)


class ProcessStatusInline(admin.TabularInline):
    model = ReserveForm
    extra = 0

class ProcessAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    inlines = [ProcessStatusInline ]

class ServiceTarhAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_display_links = ('name',)


class ProcessFormKargarAdmin(admin.ModelAdmin):
    list_display = ( 'form_code', 'customer', 'form_status', 'kargar', 'duration')
    list_display_links = ( 'form_code', 'customer',)
    search_fields = ('form__id',)

    def customer(self, obj):
        return obj.form.customer.name

    def form_code(self, obj):
        if obj.form:
            return obj.form.id
        else:
            return '-'

    def form_status(self, obj):
        if obj.process:
            return obj.process.name
        else:
            return '-'

    def kargar(self, obj):
        if obj.kargar:
            return obj.kargar.name
        else:
            return '-'

    def duration(self, obj):
        if not obj.startDateTime:
            return 'زمان شروع به درستی وارد نشده است'
        if not obj.endDateTime:
            return 'زمان اتمام به درستی وارد نشده است'
        duration = obj.endDateTime - obj.startDateTime
        hours , reminder = divmod(duration.seconds, 3600)
        return  'ساعت' + str(hours) + ' | ' + 'روز' + '\t' + str(duration.days)


    fieldsets = (
        ('سفارش',{
            'fields':('form',)
        }),
        ('فرایند',{
            'fields':('process',)
        }),
        ('کارگر',{
             'fields':('kargar',)
        }),
        ('امتیاز',{
             'fields':('rate',)
        }),
        # ('زمان شروع فرایند', {
        #     'fields':('startDay', 'startMonth', 'startYear',)
        # }),
        # ('زمان اتمام فرایند',{
        #     'fields':('endDay', 'endMonth', 'endYear',)
        # }),
        ('زمان شروع فرایند',{
            'fields':('startDateTime',)
        }),
        ('زمان اتمام فرایند',{
            'fields':('endDateTime',)
        }),
    )




class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = ('get_customer', 'message')
    readonly_fields = ('message', 'customer')

    def get_customer(self, obj):
        return obj.customer.name




admin.site.register(ReserveForm, ReserveFormAdmin)
admin.site.register(Dookht, DookhtAdmin)
admin.site.register(Chap, ChapAdmin)
admin.site.register(Parche, ParcheAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(ServiceTarh, ServiceTarhAdmin)
admin.site.register(ProcessFormKargar, ProcessFormKargarAdmin)
admin.site.register(CustomerMessage, CustomerMessageAdmin)
