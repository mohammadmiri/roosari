from .models import Kargar, Customer, KarbarKarkhane, KarbarTehran, Event

from django.contrib import admin
from django.contrib.auth.models import User, Group



class EventInline(admin.TabularInline):
    model = Event
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_name', 'phoneNumber',)
    list_display_links = ('get_name',)
    search_fields = ('get_name', 'id')
    raw_id_fields = ('user',)
    inlines = [EventInline]
    exclude = ['user']

    def get_name(self, obj):
        return obj.user.username

    def save_model(self, request, obj, form, change):
        if change == False:
            user = User.objects.create_user(username=form.cleaned_data['username'], password=12345678,
                                            email=form.cleaned_data['email'])
            obj.user = user
            obj.save()
        else:
            if 'username' in form.cleaned_data or 'email' in form.cleaned_data:
                user = obj.user
                user.username = form.cleaned_data['username']
                user.email = form.cleaned_data['email']
                user.save()
                obj.save()
            else:
                obj.save()



class KargarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)



class KarbarTehranAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name')
    list_display_links = ('id', 'username', 'name')

    def save_model(self, request, obj, form, change):
        if change == False:
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'],
                                            email = form.cleaned_data['email'])
            obj.user = user
            user.is_staff = True
            user.save()
            obj.save()
            group = Group.objects.get(name='karbarTehran')
            group.user_set.add(user)



class KarbarKharkhaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name')
    list_display_links = ('id', 'username', 'name')

    def save_model(self, request, obj, form, change):
        if change == False:
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'],
                                            email = form.cleaned_data['email'])
            obj.user = user
            user.is_staff = True
            user.save()
            obj.save()
            group = Group.objects.get(name='karbarKarkhane')
            group.user_set.add(user)




admin.site.register(Customer, CustomerAdmin)
admin.site.register(Kargar, KargarAdmin)
admin.site.register(KarbarTehran, KarbarTehranAdmin)
admin.site.register(KarbarKarkhane, KarbarKharkhaneAdmin)








