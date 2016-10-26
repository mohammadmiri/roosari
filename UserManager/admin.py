from .models import Kargar, Customer

from django.contrib import admin




class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phoneNumber',)
    list_display_links = ('name',)
    search_fields = ('name', 'id')


class KargarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Kargar, KargarAdmin)









