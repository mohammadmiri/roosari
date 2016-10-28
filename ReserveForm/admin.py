from .models import Dookht, Chap, Process, Parche, ReserveForm, ProcessFormKargar

from django.contrib import admin

# Register your models here.



class ProcessInline(admin.TabularInline):
    model = ProcessFormKargar
    extra = 1

class ReserveFormAdmin(admin.ModelAdmin):
    list_display = ()
    list_display_links = ()
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
            'fields':('typeChap', 'hasLabel',)
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
            print('مدیر')
            return ()
        elif 'کاربر تهران' in groupnames:
            print('کاربر تهران')
            return ()
        elif 'کاربر کارخانه' in groupnames:
            print('کاربر کارخانه')
            return ('customer', 'tarh', 'serviceTarh', 'hasParche', 'parche', 'parcheWidth', 'parcheHeight', 'typeChap', 'hasLabel',
                    'reserveDay', 'reserveMonth', 'reserveYear', 'deliveryDay', 'deliveryMonth', 'deliveryYear', 'description',
                    'process',)
        else:
            return ()


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


admin.site.register(ReserveForm, ReserveFormAdmin)
admin.site.register(Dookht, DookhtAdmin)
admin.site.register(Chap, ChapAdmin)
admin.site.register(Parche, ParcheAdmin)
admin.site.register(Process, ProcessAdmin)


