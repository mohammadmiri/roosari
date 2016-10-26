from .models import Kargar, Customer

from django.contrib import admin




class CustomerAdmin(admin.ModelAdmin):
    pass


class KargarAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Kargar, KargarAdmin)









