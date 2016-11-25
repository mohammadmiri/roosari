from .models import Dookht, Chap, Process, Parche, ReserveForm, ProcessFormKargar, ServiceTarh

from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.shortcuts import reverse


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


    # def get_view_on_site_url(self, obj=None):
    #     return 'http://google.com'
    #     return reverse('PrintReserveForm', kwargs={'id':obj.id})

    def get_customer_name(self, obj):
        return obj.customer.name

    # raw_id_fields = ['customer',]
    # inlines = [ProcessInline]
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
        })
    )

    formfield_overrides = {
        models.ManyToManyField: {'widget':CheckboxSelectMultiple},
    }

    def get_readonly_fields(self, request, obj=None):
        groupnames = request.user.groups.values_list('name', flat=True)
        if 'مدیر' in groupnames:
            return ()
        elif 'کاربر تهران' in groupnames:
            return ()
        elif 'کاربر کارخانه' in groupnames:
            return ('customer', 'tarh', 'serviceTarh', 'hasParche', 'parche', 'parcheWidth', 'parcheHeight', 'typeChap', 'hasLabel',
                    'reserveDay', 'reserveMonth', 'reserveYear', 'deliveryDay', 'deliveryMonth', 'deliveryYear', 'description',
                    'process',)
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
    list_display = ( 'form_code', 'customer', 'form_status', 'kargar')
    list_display_links = ( 'form_code', 'customer',)
    search_fields = ('form__id',)

    def customer(self, obj):
        return obj.form.customer.name

    def form_code(self, obj):
        return obj.form.id

    def form_status(self, obj):
        return obj.form.process.name

    def kargar(self, obj):
        return obj.kargar.name


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
        ('زمان شروع فرایند', {
            'fields':('startDay', 'startMonth', 'startYear',)
        }),
        ('زمان اتمام فرایند',{
            'fields':('endDay', 'endMonth', 'endYear',)
        }),
    )






admin.site.register(ReserveForm, ReserveFormAdmin)
admin.site.register(Dookht, DookhtAdmin)
admin.site.register(Chap, ChapAdmin)
admin.site.register(Parche, ParcheAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(ServiceTarh, ServiceTarhAdmin)
admin.site.register(ProcessFormKargar, ProcessFormKargarAdmin)

