from .models import Dookht, Chap, Process, Parche, ReserveForm, ProcessFormKargar, ServiceTarh, OtherServices
from UserManager.models import CustomerMessage


from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse
from django.conf.urls import url


class ProcessInline(admin.TabularInline):
    model = ProcessFormKargar
    extra = 0
    fieldsets = (
        ('فرایند', {
            'fields':('process',)
        }),
        ('کارگر', {
            'fields':('kargar',)
        }),
        ('زمان شروع', {
            'fields':('startDateTime',)
        }),
        ('زمان اتمام', {
            'fields':('endDateTime',)
        }),
    )


class ProcessFilter(admin.SimpleListFilter):
    title = _('فرایند')
    parameter_name = 'process'

    def lookups(self, request, model_admin):
        tuple = ()
        for process in Process.objects.all():
            tuple += (str(process.id), str(process.name))
        return tuple

    def queryset(self, request, queryset):
        for process in Process.objects.all():
            if self.value() == str(process.id):
                return ReserveForm.objects.filter(process=process)


class ReserveFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_customer_name', 'get_status', 'get_number', 'reserve_date', 'delivery_date',)
    list_display_links = ('get_customer_name',)
    search_fields = ['id', 'customer__name', 'process__name']
    inlines = [ProcessInline,]
    list_filter = (
        ('process', admin.RelatedFieldListFilter),
    )

    def get_customer_name(self, obj):
        return obj.customer.name
    get_customer_name.__name__ = 'مشتری'

    def get_status(self, obj):
        if obj.process:
            return obj.process.name
        else:
            '-'
    get_status.__name__ = 'وضعیت'

    def get_number(self, obj):
        return obj.number
    get_number.__name__ = 'تعداد'

    def delivery_date(self, obj):
        if obj.deliveryDay is not None and obj.deliveryMonth is not None and obj.deliveryYear is not None:
            return str(obj.deliveryYear)+'/'+str(obj.deliveryMonth)+'/'+str(obj.deliveryDay)
        else:
            return '-'
    delivery_date.__name__ = 'تاریخ تحویل'

    def reserve_date(self, obj):
        if obj.reserveDay is not None and obj.reserveMonth is not None and obj.reserveYear is not None:
            return str(obj.reserveYear)+'/'+str(obj.reserveMonth)+'/'+str(obj.reserveDay)
        else:
            return '-'
    reserve_date.__name__ = 'تاریخ ثبت سفارش'

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
        ('سایر خدمات', {
            'fields':('otherServices',)
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
        if 'admin' in groupnames:
            return ()
        elif 'karbarKarkhane' in groupnames:
            return ('customer', 'tarh', 'serviceTarh', 'hasParche', 'parche', 'parcheWidth', 'parcheHeight', 'typeChap', 'hasLabel',
                    'reserveDay', 'reserveMonth', 'reserveYear', 'deliveryDay', 'deliveryMonth', 'deliveryYear', 'description',
                     'dookht', 'number')
        elif 'karbarTehran' in groupnames:
            return ('process')

    def save_model(self, request, obj, form, change):
        if change == True and 'tarh' in form.changed_data:
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

    def get_readonly_fields(self, request, obj=None):
        groupnames = request.user.groups.values_list('name', flat=True)
        if 'admin' in groupnames:
            return ()
        elif 'karbarTehran' in groupnames:
            return ('customer', 'tarh', 'serviceTarh', 'hasParche', 'parche', 'parcheWidth', 'parcheHeight', 'typeChap',
                    'hasLabel',
                    'reserveDay', 'reserveMonth', 'reserveYear', 'deliveryDay', 'deliveryMonth', 'deliveryYear',
                    'description',
                    'dookht', 'number')
        elif 'karbarKarkhane' in groupnames:
            return ('customer', 'tarh', 'serviceTarh', 'hasParche', 'parche', 'parcheWidth', 'parcheHeight', 'typeChap',
                    'hasLabel',
                    'reserveDay', 'reserveMonth', 'reserveYear', 'deliveryDay', 'deliveryMonth', 'deliveryYear',
                    'description',
                    'dookht', 'number')
        else:
            return ()

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class ProcessAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    inlines = [ProcessStatusInline ]

    def get_readonly_fields(self, request, obj=None):
        groupnames = request.user.groups.values_list('name', flat=True)
        if 'admin' in groupnames:
            return ()
        elif 'karbarTehran' in groupnames:
            return ('name',)
        elif 'karbarKarkhane' in groupnames:
            return ('name',)
        else:
            return ()

class ServiceTarhAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_display_links = ('name',)


class ProcessFormKargarAdmin(admin.ModelAdmin):
    list_display = ( 'form_code', 'customer', 'form_status', 'kargar', 'duration', 'is_ended')
    list_display_links = ( 'form_code', 'customer',)
    search_fields = ('form__id',)
    raw_id_fields = ['form']
    ordering = ['-startDateTime']

    def is_ended(self, obj):
        if obj.endDateTime is not None:
            return 'تمام شده است'
        else:
            '-'
    is_ended.__name__ = 'اتمام'

    def customer(self, obj):
        return obj.form.customer.name
    customer.__name__ = 'مشتری'

    def form_code(self, obj):
        if obj.form:
            return obj.form.id
        else:
            return '-'
    form_code.__name__ = 'کد سفارش'

    def form_status(self, obj):
        if obj.process:
            return obj.process.name
        else:
            return '-'
    form_status.__name__ = 'وضعیت سفارش'

    def kargar(self, obj):
        if obj.kargar:
            return obj.kargar.name
        else:
            return '-'
    kargar.__name__ = 'کارگر'

    def duration(self, obj):
        if not obj.startDateTime:
            return '-'
        if not obj.endDateTime:
            return '-'
        duration = obj.endDateTime - obj.startDateTime
        hours , reminder = divmod(duration.seconds, 3600)
        return  str(duration.days) + '\t' + 'روز' + ' | ' + str(hours) + 'ساعت'
    duration.__name__ = 'مدت زمان'


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


class IsReadFilter(admin.SimpleListFilter):
    title = _('خواندن')
    parameter_name = 'is_read'

    def lookups(self, request, model_admin):
        tuple = (
            ('readed', _('خوانده شده است')),
            ('not readed', _('خوانده نشده است')),
        )
        return tuple

    def queryset(self, request, queryset):
        if self.value() == 'readed':
            return CustomerMessage.objects.filter(is_read=True)
        elif self.value() == 'not reader':
            return CustomerMessage.objects.filter(is_read=False)



class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = ('get_customer', 'get_date', 'get_time', 'get_message')
    readonly_fields = ('message', 'customer')
    list_filter = [IsReadFilter,]

    def get_customer(self, obj):
        return obj.customer.name
    get_customer.__name__ = 'مشتری'

    def get_message(self, obj):
        return obj.message
    get_message.__name__ = 'متن نامه'

    def get_date(self, obj):
        return obj.get_date()
    get_date.__name__ = 'تاریخ ارسال'

    def get_time(self, obj):
        return obj.get_time()
    get_time.__name__ = 'ساعت'




admin.site.register(ReserveForm, ReserveFormAdmin)
admin.site.register(Dookht, DookhtAdmin)
admin.site.register(Chap, ChapAdmin)
admin.site.register(Parche, ParcheAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(ServiceTarh, ServiceTarhAdmin)
admin.site.register(ProcessFormKargar, ProcessFormKargarAdmin)
admin.site.register(CustomerMessage, CustomerMessageAdmin)
admin.site.register(OtherServices)