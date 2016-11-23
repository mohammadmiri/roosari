from .models import Kargar, Customer, KarbarKarkhane, KarbarTehran

from django.contrib import admin
from django.contrib.auth.models import User




class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_name', 'phoneNumber',)
    list_display_links = ('get_name',)
    search_fields = ('get_name', 'id')
    raw_id_fields = ('user',)
    # actions = ['delete_model']

    def get_name(self, obj):
        return obj.user.username

    def save_model(self, request, obj, form, change):
        try:
            # creating a new model
            customer = Customer.objects.get(id=obj.id)
        except Customer.DoesNotExist:
            # changing an existing model
            user = User.objects.create_user(username=form.cleaned_data['name'], password=12345678,
                                            email=form.cleaned_data['email'])
            obj.user = user
            obj.save()


class KargarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)



class KarbarTehranAdmin(admin.ModelAdmin):
    pass


class KarbarKharkhaneAdmin(admin.ModelAdmin):
    pass



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Kargar, KargarAdmin)
admin.site.register(KarbarTehran, KarbarTehranAdmin)
admin.site.register(KarbarKarkhane, KarbarKharkhaneAdmin)








