from .models import Dookht, Chap, Process, Parche, ReserveForm, ProcessFormKargar, ServiceTarh

from django.contrib import admin




class ProcessInline(admin.TabularInline):
    model = ProcessFormKargar
    extra = 1

class ReserveFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_customer_name',)
    list_display_links = ('get_customer_name',)

    def get_customer_name(self, obj):
        return obj.customer.name

    raw_id_fields = ['customer',]
    inlines = [ProcessInline]
    fieldsets = (
        ('property', {
            'fields':('customer', )
        }),
        ('tarh', {
            'fields':('tarh', 'serviceTarh',)
        }),
        ('parche', {
            'fields':('hasParche', 'parche', )
        }),
        ('size', {
            'fields':('parcheWidth', 'parcheHeight', )
        }),
        ('property', {
            'fields':('typeChap', 'hasLabel', 'number')
        }),
        ('reserve',{
            'fields':('reserveDay', 'reserveMonth', 'reserveYear',),
        }),
        ('delivery', {
            'fields':('deliveryDay', 'deliveryMonth', 'deliveryYear', )
        }),
        ('property', {
            'fields':('description', 'process', )
        })
    )

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
        print('changed_data:'+str(form.changed_data))
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


class ProcessAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    inlines = [ProcessInline, ]

class ServiceTarhAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_display_links = ('name',)


admin.site.register(ReserveForm, ReserveFormAdmin)
admin.site.register(Dookht, DookhtAdmin)
admin.site.register(Chap, ChapAdmin)
admin.site.register(Parche, ParcheAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(ServiceTarh, ServiceTarhAdmin)


